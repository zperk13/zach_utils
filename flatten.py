def yield_flatten(iterable, stop_points=None):
    if stop_points == None:
        stop_points = [int, float, str]

    def is_stop_point(var):
        for stop_point in stop_points:
            if isinstance(var, stop_point):
                return True
        return False

    for item in iterable:
        if is_stop_point(item):
            yield item
        else:
            for subitem in yield_flatten(item):
                yield subitem


def flatten(iterable, stop_points=None):
    return_me = []
    for x in yield_flatten(iterable, stop_points):
        return_me.append(x)
    return return_me
