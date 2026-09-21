# Sistema de Registro - FastAPI + Excel Online + Telegram

Proyecto base para registrar datos desde una página web, guardarlos en Excel Online mediante Microsoft Graph y enviar una notificación mediante Telegram.

## Instalación
```bash
python -m venv .venv
pip install -r requirements.txt
```
Copia `.env.example` como `.env` y configura tus credenciales.

## Excel
Crea un archivo Excel Online con una tabla llamada `Registros` y columnas:
Nombre, Identificación, Correo, Programa, Semestre, Teléfono, Fecha.

Configura Microsoft Entra ID / Microsoft Graph y completa los datos de `.env`.

## Telegram
Crea el bot con BotFather y configura `TELEGRAM_TOKEN` y `TELEGRAM_CHAT_ID`.

## Ejecutar
```bash
uvicorn main:app --reload
```
Abre `http://127.0.0.1:8000` y la documentación en `/docs`.

## Pruebas
```bash
pytest
```
