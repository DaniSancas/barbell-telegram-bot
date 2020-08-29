from telegram_envelope.simple_text_bot import WebHookTextBot

import barbell_bot


def app(event, context):
    return WebHookTextBot(event).run(barbell_bot.barbell_logic)
