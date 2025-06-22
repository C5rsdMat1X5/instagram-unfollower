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
        input("\nInicia sesión manualmente y presiona Enter aquí cuando termines...")
        context.storage_state(path=CONTEXT_PATH)
        print(f"\nContexto guardado en {CONTEXT_PATH}")
        browser.close()

def get_info():
    username = input("Introduce tu nombre de usuario sin el @ (arroba): ").strip()
    excluded_input = input("Introduce la lista de usuarios que quieres excluir sin el @ (arroba) (formato: usuario1,usuario2,...): ").strip()
    
    excluded = [user.strip() for user in excluded_input.split(",") if user.strip()]
    
    return username, excluded

def open_followed_list(USERNAME, EXCLUIR):
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(storage_state=CONTEXT_PATH)
            page = context.new_page()
            page.goto(f"https://www.instagram.com/{USERNAME}/")
        except Exception as e:
            print(f"❌ Error inicializando navegador o contexto: {e}")
            browser.close()
            return
        
        page.wait_for_selector(f'a[href="/{USERNAME}/following/"]')
        page.click(f'a[href="/{USERNAME}/following/"]')
        time.sleep(2)

        page.wait_for_selector("div.x6nl9eh.x1a5l9x9", timeout=5000)
        container = page.query_selector("div.x6nl9eh.x1a5l9x9")

        if container is None:
            print("❌ No se encontró el contenedor principal de usuarios.")
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
                    print("❌ Se acabaron los intentos se cerrara el programa automaticamente si quieres seguir vuelve a ejecutar el programa. ")
                    time.sleep(1)
                    browser.close()
                    break
                print(
                    f"⏳ No se encontraron usuarios nuevos. Haciendo scroll para intentar cargar más...quedan {20 - tries} intentos antes de cerrar"
                )
                tries += 1
                page.mouse.wheel(0, 500)
                time.sleep(0.5)
                continue

            for user in new_users:
                try:
                    username_element = user.query_selector("span._ap3a")
                    if not username_element:
                        print("❗ No se encontró el username, se salta este usuario.")
                        continue

                    username = username_element.inner_text().strip()
                    if username in processed_usernames:
                        continue
                    processed_usernames.add(username)

                    if username in EXCLUIR:
                        print(f"⛔ Usuario excluido: {username}")
                        continue

                    button = user.query_selector("button._acan._acap._acat._aj1-._ap30")
                    if not button:
                        print("❗ No se encontró el botón, se salta este usuario.")
                        continue

                    print(f"👉 Dejando de seguir a: {username}")
                    button.click()
                    time.sleep(0.5)

                    confirm_button = page.query_selector("button._a9--._ap36._a9-_")
                    if confirm_button:
                        confirm_button.click()
                        print(f"✅ Confirmado: {username}")
                        time.sleep(0.5)

                    page.mouse.wheel(0, 60)
                    time.sleep(0.2)

                except Exception as e:
                    print(f"⚠️ Error procesando usuario: {e}")
                    continue

def main():
    parser = argparse.ArgumentParser(description="Un script que hace elimina seguidores de instagram. ")
    parser.add_argument('command', choices=['save-context', 'start'], help="Comando a ejecutar")

    args = parser.parse_args()

    if args.command == 'save-context':
        print("Guardando el contexto de sesión...")
        save_context()
    elif args.command == 'start':
        print("Iniciando el programa...")
        print(BASE_PATH)
        u, e = get_info()
        open_followed_list(u, e)
    else:
        print(f"Comando desconocido: {args.command}")

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
