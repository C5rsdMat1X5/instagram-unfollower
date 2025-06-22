# 📦 Instagram Following Remover

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Playwright](https://img.shields.io/badge/Playwright-%E2%9C%94-green?logo=playwright)

Un script en Python que automatiza la eliminación de cuentas seguidas en Instagram usando [Playwright](https://playwright.dev/python/), con exclusión de usuarios personalizados y soporte de sesión persistente.

---

## 🧠 ¿Qué hace este script?

* Abre Instagram en un navegador controlado por código.
* Usa tu sesión guardada para acceder a tu cuenta.
* Va a tu lista de seguidos.
* Hace scroll automático hasta encontrar nuevos usuarios.
* Elimina (deja de seguir) a cada cuenta, excepto las que tú excluyas.

---

## ⚙️ Requisitos

* Python 3.10 o superior
* [Playwright](https://playwright.dev/python/)

---

## 🛠️ Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/tuusuario/instagram-following-remover.git
cd instagram-following-remover
```

2. Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
playwright install
```

---

## 🚀 Cómo usar

### 1. Guardar el contexto de sesión

```bash
python instagram-followin-remover.py save-context
```

Esto abrirá Instagram en una ventana. Inicia sesión manualmente y luego presiona `Enter` en la consola.

Esto guardará tu sesión en `instagram_storage_state.json`.

---

### 2. Eliminar seguidos automáticamente

```bash
python instagram-followin-remover.py start
```

El script te pedirá:

* Tu nombre de usuario (sin @).
* La lista de usuarios a excluir, separados por coma.

**Ejemplo:**

```
Introduce tu nombre de usuario sin el @ (arroba): m4ti.14s  
Introduce la lista de usuarios que quieres excluir sin el @ (arroba) (formato: usuario1,usuario2,...): juan,pedro,ana
```

El script empezará a dejar de seguir a todas las cuentas que no estén en la lista de exclusión.

---

## 📁 Estructura de archivos

```
instagram-following-remover/
│
├── instagram-followin-remover.py
├── instagram_storage_state.json  # Se crea después de guardar el contexto
├── requirements.txt
└── README.md
```

---

## 🛯️ Notas

* Instagram puede cambiar sus clases HTML en cualquier momento.
* Este script no es oficial ni aprobado por Instagram.
* Úsalo bajo tu propio riesgo. Evita automatizar en exceso para no ser baneado.

---

## 🎨 Extra: ASCII Style

Este script incluye un mini arte ASCII de Instagram en la terminal para que se vea pro al arrancar 🧓

---

## ✍️ Autor

Hecho con rabia y sarcasmo por [@m4ti.14s](https://github.com/m4tiashenriquez)
