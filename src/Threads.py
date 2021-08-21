from threading import Thread

from src import HourlyCheck


def startThreads():
    """
    Start the hourly threads.
    """
    # start the hourly check thread
    every_hour_plus_1minute_thread = Thread(target=HourlyCheck.everyHourCheck_OneMinuteDelay)
    every_hour_plus_1minute_thread.start()
    every_hour_plus_15secs_thread = Thread(target=HourlyCheck.everyHourCheck_15SecsDelay)
    every_hour_plus_15secs_thread.start()