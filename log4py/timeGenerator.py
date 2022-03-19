from datetime import datetime


def timeGenerator(timeFormat):
    return datetime.now().strftime(timeFormat)
