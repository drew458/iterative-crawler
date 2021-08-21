from threading import Thread

from src import Stats, TimeElapsed, NotificationConsole, Scraper, CheckKeywords, HourlyCheck, IOConsole


def mode1(url, inputText, waitTime):
    """
    Runs the scraper in Mode 1. That means, when the string is found on the website it sends notification; if the string
    isn't found, continues to search.
    :param url: the url of the website.
    :param inputText: the text to look for on the website.
    :param waitTime: the time to wait between one check and another.
    """
    count = 0
    days = 0
    weeks = 0

    # while this is true (it is true by default)
    while True:

        # start the timer for execution statistics
        start_scrape = Stats.performanceCounter()

        # scrape the page
        scrapedPage = Scraper.scrapeThePage(url)

        # find the string
        # strings = Scraper.retainStrings(scrapedPage, inputText)

        # start the timer for execution statistics
        finish_scrape = Stats.performanceCounter()

        # start collecting stats about the conditional statement (if) performance
        start_conditional_statement = Stats.performanceCounter()

        # start the hourly check thread
        every_hour_plus_1minute_thread = Thread(target=HourlyCheck.everyHourCheck_OneMinuteDelay)
        every_hour_plus_1minute_thread.start()
        every_hour_plus_15secs_thread = Thread(target=HourlyCheck.everyHourCheck_15SecsDelay)
        every_hour_plus_15secs_thread.start()

        # if the keywords are in the page... object found!
        if CheckKeywords.check(scrapedPage, inputText) is True:
            IOConsole.printFoundMessage()

            # To enable Windows notifications, uncomment the line below
            # swn.sendNotification()

            # Telegram bot notification
            NotificationConsole.sendTelegramNotification(IOConsole.getFoundMessageTelegram())

            # OS notification
            NotificationConsole.sendOSNotification(IOConsole.getFoundTitle(), IOConsole.getFoundMessage())

            # Adiòs
            break

        # if the keywords are still there, keep searching...
        else:
            count = count + 1
            IOConsole.printCheckNumberMessage(count)

            # finish collecting stats about the conditional statement (if) performance
            finish_conditional_statement = Stats.performanceCounter()

            # Show stats
            IOConsole.printWaitingStatsMessage()
            TimeElapsed.checkDaysWeeksElapsed(count, days, weeks)
            Stats.printPerformanceResult(Stats.getResult(start_scrape, finish_scrape))
            Stats.printConditionalStatementResult(
                Stats.getResult(start_conditional_statement, finish_conditional_statement))
            print()

            # wait the time defined as input
            # time.sleep(600)
            TimeElapsed.countdown(int(waitTime))

            # continue with the script (that is, go back at the top of the while loop)
            continue


def mode2(url, inputText, waitTime):
    """
    Runs the scraper in Mode 2. That means, when the string is found on the website, continues to search.
    If the string isn't found, it sends notification and stops.
    :param url: the url of the website.
    :param inputText: the text to look for on the website.
    :param waitTime: the time to wait between one check and another.
    """
    count = 0
    days = 0
    weeks = 0

    # while this is true (it is true by default)
    while True:

        # start the timer for execution statistics
        start_scrape = Stats.performanceCounter()

        # scrape the page
        scraped_page = Scraper.scrapeThePage(url)

        # find the string
        strings = Scraper.retainStrings(scraped_page, inputText)

        # start the timer for execution statistics
        finish_scrape = Stats.performanceCounter()

        # start collecting stats about the conditional statement (if) performance
        start_conditional_statement = Stats.performanceCounter()

        # start the hourly check thread
        every_hour_plus_1minute_thread = Thread(target=HourlyCheck.everyHourCheck_OneMinuteDelay)
        every_hour_plus_1minute_thread.start()
        every_hour_plus_15secs_thread = Thread(target=HourlyCheck.everyHourCheck_15SecsDelay)
        every_hour_plus_15secs_thread.start()

        # if the keywords are still there, keep searching...
        if CheckKeywords.check(strings, inputText) is True:
            count = count + 1
            IOConsole.printCheckNumberMessage(count)

            # finish collecting stats about the conditional statement (if) performance
            finish_conditional_statement = Stats.performanceCounter()

            # Show stats
            IOConsole.printWaitingStatsMessage()
            TimeElapsed.checkDaysWeeksElapsed(count, days, weeks)
            Stats.printPerformanceResult(Stats.getResult(start_scrape, finish_scrape))
            Stats.printConditionalStatementResult(
                Stats.getResult(start_conditional_statement, finish_conditional_statement))
            print()

            # wait the time defined as input
            # time.sleep(600)
            TimeElapsed.countdown(int(waitTime))

            # continue with the script (that is, go back at the top of the while loop)
            continue

        # but if the words above don't occur... object found!
        else:
            IOConsole.printStartMessage()

            # To enable Windows notifications, uncomment the line below
            # swn.sendNotification()

            # Telegram bot notification
            NotificationConsole.sendTelegramNotification(IOConsole.getFoundTitle(), IOConsole.getFoundMessage())

            # OS notification
            NotificationConsole.sendOSNotification(IOConsole.getFoundTitle(), IOConsole.getFoundMessage())

            # Adiòs
            break
