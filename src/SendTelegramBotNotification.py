import os
from urllib.parse import quote_plus
import requests

from src.static import Keys


def sendNotification(found_message):
    """
    Sends a Telegram notification via a bot.
    """

    # Retain the Telegram Bot token from environment variables
    try:
        TOKEN = os.environ["TOKEN"]
    except KeyError:
        TOKEN = Keys.token

    # Retain the Telegram chat_id from environment variables
    try:
        CHAT_ID = os.environ["CHAT_ID"]
    except KeyError:
        CHAT_ID = Keys.chat_id

    # Send notification
    notification_url = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s' % (
        TOKEN, CHAT_ID, quote_plus(found_message))
    _ = requests.get(notification_url, timeout=10)
