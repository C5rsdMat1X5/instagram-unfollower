# 📦 Instagram Following Remover

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)  
![Playwright](https://img.shields.io/badge/Playwright-%E2%9C%94-green?logo=playwright)

A Python script that automates unfollowing accounts on Instagram using [Playwright](https://playwright.dev/python/), with support for custom user exclusions and persistent session.

---

## 🧠 What does this script do?

* Opens Instagram in a programmatically controlled browser.  
* Uses your saved session to access your account.  
* Goes to your following list.  
* Automatically scrolls until it finds new users.  
* Unfollows each account except the ones you exclude.

---

## ⚙️ Requirements

* Python 3.10 or higher  
* [Playwright](https://playwright.dev/python/)

---

## 🛠️ Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/instagram-following-remover.git
cd instagram-following-remover
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
playwright install
```

---

## 🚀 How to use

### 1. Save session context

```bash
python instagram-followin-remover.py save-context
```

This will open Instagram in a window. Log in manually and then press `Enter` in the console.

This saves your session in `instagram_storage_state.json`.

---

### 2. Automatically unfollow accounts

```bash
python instagram-followin-remover.py start
```

The script will ask for:

* Your username (without the @ symbol).  
* The list of users to exclude, separated by commas.

**Example:**

```
Enter your username without the @ symbol: m4ti.14s  
Enter the list of users you want to exclude without the @ symbol (format: user1,user2,...): juan,pedro,ana
```

The script will start unfollowing all accounts not on the exclusion list.

---

## 📁 File structure

```
instagram-following-remover/
│
├── instagram-followin-remover.py
├── instagram_storage_state.json  # Created after saving the session context
├── requirements.txt
└── README.md
```

---

## 🛯️ Notes

* Instagram can change its HTML classes at any time.  
* This script is unofficial and not approved by Instagram.  
* Use at your own risk. Avoid excessive automation to prevent being banned.

---

## 🎨 Extra: ASCII Style

This script includes a mini ASCII Instagram art in the terminal to look pro on startup 🧓

---

## ✍️ Author

Made with rage and sarcasm by [@m4ti.14s](https://github.com/m4tiashenriquez)
