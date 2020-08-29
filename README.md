# Barbell Telegram Bot
- English: A Telegram bot for barbell plates load calculations (current output in spanish)
- Castellano: Un bot de Telegram para calcular la carga de discos en una barra olímpica (interacción actual en castellano)

## How to use (spanish below)
1. Open a conversation to [@barbell_bot](https://t.me/barbell_bot) on Telegram
2. Start with one of the following commands `/start`, `/ayuda` (help) or `/eco` (echo)
3. To calculate which plates to load, type the `/kg` command followed by a number, with `.` (dot) separator for decimals if needed. 
Example: `/kg 102.5`
4. In this example, the response will tell you to load 41.25kg to each side, with the following plate weights: 25, 15, 1.25

Note: The bot assumes you are using an standard olympic barbell (20kg).

## How internally works
This bot uses the [telegram-envelope](https://github.com/DaniSancas/telegram-envelope) Python package for managing the bot, along with the [serverless framework](https://github.com/serverless/serverless) to interact with AWS Lambda environment.

---

## Cómo interactuar con Barbell Bot
1. Abre una conversación con [@barbell_bot](https://t.me/barbell_bot) en Telegram
2. Escribe uno de los siguientes comandos `/start`, `/ayuda` o `/eco`.
3. Para calcular qué discos cargar en la barra, escribe el comando `/kg` seguido de un número, con un `.` (punto) para la separación de decimales.
Ejemplo: `/kg 102.5`
4. En este caso, el bot te responderá que debes cargar 41.25kg a cada lado, con discos de los siguientes pesos: 25, 15, 1.25

Nota: El bot da por hecho que estás usando una barra olímpica convencional (20kg).

### Cómo funciona internamente
Este bot utiliza el paquete de Python [telegram-envelope](https://github.com/DaniSancas/telegram-envelope) para gestionar el bot, junto con el [framework serverless](https://github.com/serverless/serverless) para interactuar con el entorno de AWS Lambda.
