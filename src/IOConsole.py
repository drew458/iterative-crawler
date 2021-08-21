START_MESSAGE = "HI! This is a general scraper.\n" \
                "It can work in two ways: send notification if text is found on the page, or waiting and keep refreshing until the text " \
                "goes away from the page."
FOUND_TITLE = "FOUND IT!"
FOUND_MESSAGE = "The situation on the website you are monitoring has changed. Please go check it out."
FOUND_MESSAGE_TELEGRAM = "FOUND IT! The situation on the website you are monitoring has changed. Please go check it out."


def inputUrl():
    """
    Sets the URL
    :return: the URL
    """
    url = input("Please insert the website URL to scrape...\n")
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
    """
        The operating mode of the scraper.
        It can either send notification if text is found on the page, or waiting and keep refreshing
        until the text goes away from the page.
        :return: the mode
        """
    print("In which mode should the scraper behave?\nInsert the corresponding number...")
    print("1. Send a notification when the text inserted is found in the website")
    print("2. Send a notification when the text inserted isn't on the website anymore")
    mode = input()

    return mode


def printStartMessage():
    print(START_MESSAGE)
    print()


def printFoundMessage():
    print(FOUND_TITLE)


def printCheckNumberMessage(count):
    print("Check number", count, ", nothing found, I won't give up...")


def printWaitingStatsMessage():
    print("While waiting, let's see some stats about the execution...")


def getFoundTitle():
    return FOUND_TITLE


def getFoundMessage():
    return FOUND_MESSAGE


def getFoundMessageTelegram():
    return FOUND_MESSAGE_TELEGRAM
