from time import time


class TimeTracker(object):
    def __init__(self):
        global TimeTracker_start_time
        TimeTracker_start_time = time()

    def stop():
        return (time() - TimeTracker_start_time)


# How to use:
# from zach_utils.TimeTracker import TimeTracker
# TimeTracker()
# <code that you want to see how long it takes>
# print(TimeTracker.stop())
