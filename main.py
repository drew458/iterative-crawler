import sys

from src import IOConsole, ScraperMode, UserInputConfiguration

""" The script scrapes the page inserted as user input URL, looking for the text inserted as user input.
    Then it can either send notification if text is found on the page, or waiting and keep refreshing until the text
    goes away from the page. The mode choice is inserted as user input. 
    When triggered, it can send notification via screen, OS, Telegram. 
"""


def main():

    IOConsole.printStartMessage()

    url, inputText, waitTime, mode, emailAddress = UserInputConfiguration.programStart()

    if int(mode) == 1:
        ScraperMode.mode1(url, inputText, waitTime, emailAddress)

    if int(mode) == 2:
        ScraperMode.mode2(url, inputText, waitTime, emailAddress)

    sys.exit()


if __name__ == "__main__":
    main()
