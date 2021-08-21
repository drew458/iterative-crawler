import platform
import os
from plyer import notification
from urllib.parse import quote_plus
import requests

from src.static import Keys

# TODO: aggiungere notifiche via email


def sendTelegramNotification(found_message, title=None):
    """
    Sends a Telegram notification via a bot.
    :param title: the title of notification
    :param found_message: the message of notification
    """

    # Retain the Telegram Bot TOKEN from environment variables or Python file
    try:
        TOKEN = os.environ["TOKEN"]
    except KeyError:
        TOKEN = Keys.token

    # Retain the Telegram CHAT_ID from environment variables or Python file
    try:
        CHAT_ID = os.environ["CHAT_ID"]
    except KeyError:
        CHAT_ID = Keys.chat_id

    if title is not None:
        # Send title notification
        notification_url = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s' % (
            TOKEN, CHAT_ID, quote_plus(title))
        _ = requests.get(notification_url, timeout=10)

    # Send found_message notification
    notification_url = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s' % (
        TOKEN, CHAT_ID, quote_plus(found_message))
    _ = requests.get(notification_url, timeout=10)


def sendOSNotification(title, found_message):
    """
    Sends as OS-independent notification.
    :param title: the title of notification
    :param found_message: the message of notification
    """
    notification.notify(
        title=title,
        message=found_message,
        app_name="General Scraper",
    )


def sendWindowsNotification(title, found_message):
    """
    Sends as Windows system notification.
    :param title: the title of notification
    :param found_message: the message of notification
    """

    if platform.system() == "Windows":
        from win10toast import ToastNotifier

        toaster = ToastNotifier()
        toaster.show_toast(title, found_message)


def notify(title, found_message):
    """
    Sends as MacOS system notification.
    :param title: the title of notification
    :param found_message: the message of notification
    """
    if platform.system() == "Darwin":
        os.system("""
                  osascript -e 'display notification "{}" with title "{}"'
                  """.format(found_message, title))

    notify("Title", found_message)
