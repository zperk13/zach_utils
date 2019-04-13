from datetime import datetime


def datetime_dict():
    # Returns a dictionary for the time info at the second the function is run
    now = datetime.now()
    return {'year': now.year, 'month': now.month, 'day': now.day, 'hour': now.hour, 'minute': now.minute,
            'second': now.second}


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def is_now_leap_year():
    return is_leap_year(datetime_dict()['year'])


def day_of_year():
    # Returns the day of year at the day of function running
    return datetime.now().timetuple().tm_yday


def year_percentage():
    day_of_year_var = day_of_year()
    if is_now_leap_year():
        print(day_of_year_var / 366 * 100)
    else:
        print(day_of_year_var / 365 * 100)
    print(day_of_year_var)
