import schedule
import datetime
import time
from src import Scraper, CheckKeywords, NotificationConsole, IOConsole


def job():
    """
    Scrapes the page, checks if the string inseide the tags is present and then sends a notification.
    """
    # Scrape the page
    scraped_page = Scraper.scrapeThePage()

    # Find the H1 tags
    strings_h1 = Scraper.retainStrings(scraped_page)

    # Keywords
    texth1 = 'Le console sono in arrivo. Continua a seguirci per scoprire quando la vendita sarà aperta.'
    texth3 = 'Le tue console preferite torneranno disponibili nelle prossime settimane su questo sito.'

    if not CheckKeywords.check(strings_h1, texth1) is True:
        print(IOConsole.getSystemFoundTitle())

        # Windows notification
        # swn.sendNotification()

        # Telegram bot notification
        NotificationConsole.sendTelegramNotification(IOConsole.getSystemFoundTitle())
    else:
        print("Hourly check of " + datetime.datetime.now().strftime("%H") + ":" + datetime.datetime.now().strftime("%M")
              + ":" + datetime.datetime.now().strftime("%S") + ", nothing found...")
        print()


def everyHourCheck_15SecsDelay():
    """
    Does the complete job of scraping and sending a notification, every hour and 15 secs.
    """
    schedule.every().day.at("00:00:15").do(job)
    schedule.every().day.at("01:00:15").do(job)
    schedule.every().day.at("02:00:15").do(job)
    schedule.every().day.at("03:00:15").do(job)
    schedule.every().day.at("04:00:15").do(job)
    schedule.every().day.at("05:00:15").do(job)
    schedule.every().day.at("06:00:15").do(job)
    schedule.every().day.at("07:00:15").do(job)
    schedule.every().day.at("08:00:15").do(job)
    schedule.every().day.at("09:00:15").do(job)
    schedule.every().day.at("10:00:15").do(job)
    schedule.every().day.at("11:00:15").do(job)
    schedule.every().day.at("12:00:15").do(job)
    schedule.every().day.at("13:00:15").do(job)
    schedule.every().day.at("14:00:15").do(job)
    schedule.every().day.at("15:00:15").do(job)
    schedule.every().day.at("16:00:15").do(job)
    schedule.every().day.at("17:00:15").do(job)
    schedule.every().day.at("18:00:15").do(job)
    schedule.every().day.at("19:00:15").do(job)
    schedule.every().day.at("20:00:15").do(job)
    schedule.every().day.at("21:00:15").do(job)
    schedule.every().day.at("22:00:15").do(job)
    schedule.every().day.at("23:00:15").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


def everyHourCheck_OneMinuteDelay():
    """
    Does the complete job of scraping and sending a notification, every hour and a minute.
    """
    schedule.every().hour.at(":01").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
