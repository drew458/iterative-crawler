# Iterative-scraper

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![MIT License](https://img.shields.io/github/license/drew458/iterative-scraper?style=for-the-badge)](https://opensource.org/licenses/MIT)  

A scraper that looks for specific text in a website and sends notifications when the text appears or disappears. The website, the text and the operating mode is inserted as user input when the program starts.  
The script is compatible with Python 3.x versions.

## Configuration

Before starting the script, you need to install the following external modules through CLI (Windows/Linux/Mac):
* `pip3 install -r requirements.txt`

To run the script, `cd` into the folder and `python3 main.py`.

## Notifications

Various types of notifications are available and ready to use:
* ### On screen notifications.
* ### System notifications 
    No matter your operating system, there's built-in support for native notifications.
* ### Telegram bot notifications
  You can either set `TOKEN` and `CHAT_ID` as environment variables or create a file `Keys.py` with those variables.  
  If you're thinking to deploy it on Heroku, see below.

## Usage & Features

When you start the program, you are prompted to insert:
* Website URL
* Text to look for on the website
* Operating mode (notification sent when text appears or disappears)
* Time from one check to another (that is, delay)

## Cloud deployment

The script is ready for deployment on Heroku, which is what I use to run it on the cloud and get the Telegram bot notifications.  
The free tier on Heroku perfectly fits. In this case the bot token and chat it must go into the virtual environment variables (see the settings page on Heroku's dashboard).

## Future Updates

* Add email notifications
* Add more parameters for the type of strings of text to look for
* Displaying some more stats about the usage and elapsed time
* Add a GUI
