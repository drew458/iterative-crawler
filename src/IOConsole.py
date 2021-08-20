FOUND_MESSAGE = "FOUND IT!"
START_MESSAGE = "HI! I'm a scraper"


def printStartMessage():
    print(START_MESSAGE)
    print()


def inputUrl():
    """
    Sets the URL
    :return: the URL
    """
    url = input("Please insert the website URL where you want to scrape...\n")
    print()
    return url


def inputKeywords():
    """
    Keywords to look for
    :return: the keywords
    """
    inputText = input("Please insert the text to look for on the website...\n")
    print()
    return inputText


def inputTimeToSleep():
    """
    Time from one check to another
    :return: the time
    """
    sleepTime = input("Please insert the time (in seconds) to wait between checks...\n")
    print()
    return sleepTime


def scraperMode():
    print("In which mode should the scraper behave?\nInsert the correspondant number...")
    print("1. Send a notification when the text inserted is found in the webiste")
    print("2. Send a notification when the text inserted isn't there anymore")
    mode = input()

    return mode


def printFoundMessage():
    print(FOUND_MESSAGE)


def printCheckNumberMessage(count):
    print("Check number", count, ", nothing found, I won't give up...")


def printWaitingStatsMessage():
    print("While waiting, let's see some stats about the execution...")


def getFoundMessage():
    return FOUND_MESSAGE
