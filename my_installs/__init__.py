import time
from random import uniform


def addNumbers(number1, number2):
    """
    Provide two numbers and I'll add them together
    """
    return number1 + number2


def timer(start_time, end_time):
    """
    Timer to snooze while scraping
    Para_1: start_time: integer for minimum seconds snooze
    Para_2: end_time: integer for maximum seconds snooze
    """
    snoozer = uniform(start_time, end_time)
    print(f"Snoozing for {snoozer} seconds!")
    time.sleep(snoozer)