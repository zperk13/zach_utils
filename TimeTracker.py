from time import time


class TimeTracker(object):
    def __init__(self):
        global start_time
        start_time = time()

    def stop():
        return(time() - start_time)


# How to use:
# from zach_utils.TimeTracker import TimeTracker
# TimeTracker()
# <code that you want to see how long it takes>
# print(TimeTracker.stop())