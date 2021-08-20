from src import IOConsole, scraperModes

""" This is a really simple script. The script downloads the page of MediaWorld where the PS5 Digital Edition 
    will be added when available, and if found, notifies via Telegram bot.
    If nothing is found it repeats after 10 minutes.
"""


# To enable Windows notifications, uncomment line below
# import sendWindowsNotification as swn


def main():

    IOConsole.printStartMessage()

    # set the url
    url = IOConsole.inputUrl()

    # keywords to look for
    inputText = IOConsole.inputKeywords()

    # time from one check to another
    waitTime = IOConsole.inputTimeToSleep()

    mode = IOConsole.scraperMode()

    if int(mode) == 1:
        scraperModes.mode1(url, inputText, waitTime)

    if int(mode) == 2:
        scraperModes.mode2(url, inputText, waitTime)


if __name__ == "__main__":
    main()
