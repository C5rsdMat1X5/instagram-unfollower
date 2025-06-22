from playwright.sync_api import sync_playwright
import time
import argparse
import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
CONTEXT_PATH = os.path.join(BASE_PATH, "instagram_storage_state.json")

def save_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.instagram.com/")
        input("\nLog in manually and press Enter here when you are done...")
        context.storage_state(path=CONTEXT_PATH)
        print(f"\nContext saved at {CONTEXT_PATH}")
        browser.close()

def get_info():
    username = input("Enter your username without the @ symbol: ").strip()
    excluded_input = input("Enter the list of users you want to exclude without the @ symbol (format: user1,user2,...): ").strip()
    
    excluded = [user.strip() for user in excluded_input.split(",") if user.strip()]
    
    return username, excluded

def open_followed_list(USERNAME, EXCLUDE):
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(storage_state=CONTEXT_PATH)
            page = context.new_page()
            page.goto(f"https://www.instagram.com/{USERNAME}/")
        except Exception as e:
            print(f"❌ Error initializing browser or context: {e}")
            browser.close()
            return
        
        page.wait_for_selector(f'a[href="/{USERNAME}/following/"]')
        page.click(f'a[href="/{USERNAME}/following/"]')
        time.sleep(2)

        page.wait_for_selector("div.x6nl9eh.x1a5l9x9", timeout=5000)
        container = page.query_selector("div.x6nl9eh.x1a5l9x9")

        if container is None:
            print("❌ Main user container not found.")
            return

        users = container.query_selector_all("div > div > div")

        processed_usernames = set()
        
        tries = 0

        while True:
            users = container.query_selector_all("div > div > div")
            new_users = []

            for user in users:
                username_element = user.query_selector("span._ap3a")
                if not username_element:
                    continue
                username = username_element.inner_text().strip()
                if username not in processed_usernames:
                    new_users.append(user)

            if not new_users:
                if tries > 20:
                    print("❌ No new users found, closing the program automatically. If you want to continue, please run the program again.")
                    time.sleep(1)
                    browser.close()
                    break
                print(
                    f"⏳ No new users found. Scrolling to try to load more... {20 - tries} attempts left before closing."
                )
                tries += 1
                page.mouse.wheel(0, 500)
                time.sleep(0.5)
                continue

            for user in new_users:
                try:
                    username_element = user.query_selector("span._ap3a")
                    if not username_element:
                        print("❗ Username not found, skipping this user.")
                        continue

                    username = username_element.inner_text().strip()
                    if username in processed_usernames:
                        continue
                    processed_usernames.add(username)

                    if username in EXCLUDE:
                        print(f"⛔ User excluded: {username}")
                        continue

                    button = user.query_selector("button._acan._acap._acat._aj1-._ap30")
                    if not button:
                        print("❗ Button not found, skipping this user.")
                        continue

                    print(f"👉 Unfollowing: {username}")
                    button.click()
                    time.sleep(0.5)

                    confirm_button = page.query_selector("button._a9--._ap36._a9-_")
                    if confirm_button:
                        confirm_button.click()
                        print(f"✅ Confirmed: {username}")
                        time.sleep(0.5)

                    page.mouse.wheel(0, 60)
                    time.sleep(0.2)

                except Exception as e:
                    print(f"⚠️ Error processing user: {e}")
                    continue

def main():
    parser = argparse.ArgumentParser(description="A script that unfollows Instagram users.")
    parser.add_argument('command', choices=['save-context', 'start'], help="Command to execute")

    args = parser.parse_args()

    if args.command == 'save-context':
        print("Saving session context...")
        save_context()
    elif args.command == 'start':
        print("Starting the program...")
        print(BASE_PATH)
        u, e = get_info()
        open_followed_list(u, e)
    else:
        print(f"Unknown command: {args.command}")

if __name__ == "__main__":
    print("""
    ___           _                                  
    |_ _|_ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___  
    | || '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \ 
    | || | | \__ \ || (_| | (_| | | | (_| | | | | | |
    |___|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_|
                            |___/                     
    """)
    main()
    del os, time, argparse