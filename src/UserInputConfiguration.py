from src import IOConsole


def programStart():
    """
    The prompted configuration at the start of the program.
    :return: url: the URL of the website
    :return: inputText: the string of text to look for on the website
    :return: waitTime: the time delay between two scrapes
    :return: mode: the operating mode of the script
    """
    # set the url
    url = IOConsole.inputUrl()

    # keywords to look for
    inputText = IOConsole.inputKeywords()

    # time from one check to another
    waitTime = IOConsole.inputTimeToSleep()

    # operating mode of the script
    mode = IOConsole.scraperMode()

    # the address to send email notification
    emailAddress = IOConsole.inputReceiverEmailAddress()

    return url, inputText, waitTime, mode, emailAddress
