
from src import Stats, TimeElapsed, NotificationConsole, Scraper, CheckKeywords, Threads, IOConsole


def pageScrapingAndStats(url):
    """
    Scrapes the page and collect statistics about the execution.
    :param url: the URL of the website
    :return: scrapedPage: the page scraped as a string
    :return: start_scrape: the time elapsed (in seconds) since the execution of the program when the scraping timer starts
    :return: finish_scrape: the time elapsed (in seconds) since the execution of the program when the scraping timer ends
    :return: start_conditional_statement: the time elapsed (in seconds) since the execution of the program when the
            conditional statement timer
    """
    # start the timer for execution statistics
    start_scrape = Stats.performanceCounter()

    # scrape the page
    scrapedPage = Scraper.scrapeThePage_JSSupport(url)

    # find the string
    # strings = Scraper.retainStrings(scrapedPage, inputText)

    # start the timer for execution statistics
    finish_scrape = Stats.performanceCounter()

    # start collecting stats about the conditional statement (if) performance
    start_conditional_statement = Stats.performanceCounter()

    return scrapedPage, start_scrape, finish_scrape, start_conditional_statement


def sendAllNotifications():
    """
    Sends the notification on all the platforms
    """
    # To enable Windows notifications, uncomment the line below
    # swn.sendNotification()

    # Telegram bot notification
    NotificationConsole.sendTelegramNotification(IOConsole.getFoundMessageTelegram())

    # OS notification
    NotificationConsole.sendOSNotification(IOConsole.getFoundTitle(), IOConsole.getFoundMessage())


def KeepSearching(count, days, weeks, start_scrape, finish_scrape, start_conditional_statement, waitTime):
    """
    Chunk to code to be executed when it keeps searching.
    :param count: an iterator
    :param days: days passed since the start
    :param weeks: weeks passed since the start
    :param start_scrape: the time elapsed (in seconds) since the execution of the program when the scraping timer starts
    :param finish_scrape: the time elapsed (in seconds) since the execution of the program when the scraping timer ends
    :param start_conditional_statement: the time elapsed (in seconds) since the execution of the program when the
            conditional statement timer
    :param waitTime: the time to wait between two scrapes.

    :return: count: the iterator
    """
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

    return count


def ObjectFound():
    """
    Chunk to code to be executed when the keywords are found in the website.
    """
    IOConsole.printFoundMessage()

    sendAllNotifications()


def mode1(url, inputText, waitTime):
    """
    Runs the scraper in Mode 1. That means, when the user-inserted string is found on the website it sends notification;
    if the string isn't found, continues to search.
    :param url: the url of the website.
    :param inputText: the text to look for on the website.
    :param waitTime: the time to wait between one check and another.
    """
    count = 0
    days = 0
    weeks = 0

    # start the hourly check thread
    Threads.startThreads()

    # while this is true (it is true by default)
    while True:

        scrapedPage, start_scrape, finish_scrape, start_conditional_statement = pageScrapingAndStats(url)

        # if the keywords are in the page... object found!
        if CheckKeywords.checkJS(scrapedPage, inputText) is True:
            ObjectFound()

            # Adiòs
            break

        # if the keywords aren't in the page, keep searching...
        else:
            count = KeepSearching(count, days, weeks, start_scrape, finish_scrape, start_conditional_statement, waitTime)

            # continue with the script (that is, go back at the top of the while loop)
            continue


def mode2(url, inputText, waitTime):
    """
    Runs the scraper in Mode 2. That means, when the user-inserted text is on the website, continues to search.
    If the text isn't found, it sends notifications and stops.
    :param url: the url of the website.
    :param inputText: the text to look for on the website.
    :param waitTime: the time to wait between one check and another.
    """
    count = 0
    days = 0
    weeks = 0

    # start the hourly check thread
    Threads.startThreads()

    # while this is true (it is true by default)
    while True:

        # scrape the page and collect stats
        scrapedPage, start_scrape, finish_scrape, start_conditional_statement = pageScrapingAndStats(url)

        # if the keywords are still int the page, keep searching...
        if CheckKeywords.checkJS(scrapedPage, inputText) is True:
            count = KeepSearching(count, days, weeks, start_scrape, finish_scrape, start_conditional_statement, waitTime)

            # continue with the script (that is, go back at the top of the while loop)
            continue

        # but if the words above don't occur in the page... object found!
        else:
            IOConsole.printStartMessage()

            sendAllNotifications()

            # Adiòs
            break
