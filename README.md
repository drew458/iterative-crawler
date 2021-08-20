# Iterative-scraper

[![MIT License](https://img.shields.io/github/license/drew458/ps5-scraper)](https://opensource.org/licenses/MIT)

A scraper that looks for specific text in a website and sends notifications when the text appears or disappears. The website, the text and the operating mode is inserted as user input when the program starts.  
The script is compatible with Python 3.x versions.

## Configuration

Before starting the script, you need to install the following external modules through CLI (Windows/Linux/Mac):
* `pip3 install requests` (HTTP(S) requests)

More briefly, just run:
* `pip3 install -r requirements.txt`

To run the script, `cd` into the folder and `python3 main.py`.

## Notifications

Various types of notifications are available and ready to use:
* On screen notifications.
* Windows system notifications (you just need to uncomment one line of code).
* Telegram bot notifications (change where your bot `token` and `chat_id` are stored; if you're thinking to deploy it on Heroku, see below).

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
* Support every os with system notification
* Add more parameters for specific or general strings of text to look for
* Displaying some more stats about the usage and elapsed time
* Add a GUI
