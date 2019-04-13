# Different ways of generating pi

import math

from tqdm import trange

from zach_utils.TimeTracker import TimeTracker


def Gregory_Leibniz(max_num, progress_bar=False):
    if progress_bar:
        pi = 4 / 1
        add = False
        for x in trange(3, max_num + 1, 2, desc='Gregory_Leibniz calculation'):
            if add:
                pi += 4 / x
                add = False
            else:
                pi -= 4 / x
                add = True
        return pi
    else:
        pi = 4 / 1
        add = False
        for x in range(3, max_num + 1, 2):
            if add:
                pi += 4 / x
                add = False
            else:
                pi -= 4 / x
                add = True
        return pi


def Nilakantha(max_num):
    num1 = 2
    num2 = 3
    num3 = 4
    pi = 3
    add = True
    while num3 < max_num:
        if add:
            pi += 4 / (num1 * num2 * num3)
            add = False
        else:
            pi -= 4 / (num1 * num2 * num3)
            add = True
        num1 += 2
        num2 += 2
        num3 += 2
    return pi


def limit(max_num):
    pi = math.radians(max_num * math.sin(180 / max_num))
    return pi


if __name__ == '__main__':
    TimeTracker()
    gl_var = Gregory_Leibniz(1_000_000)
    n_var = Nilakantha(1_000_000)
    l_var = limit(1_000_000)
    print(TimeTracker.stop())
    print('Gregory_Leibniz:', gl_var)
    print('Nilakantha:', n_var)
    print('Limit:', l_var)
    print('Math Module:', math.pi)

    gl_diff = abs(math.pi - gl_var)
    n_diff = abs(math.pi - n_var)
    l_diff = abs(math.pi - l_var)

    diff_list = []
    diff_list.append(gl_diff)
    diff_list.append(n_diff)
    diff_list.append(l_diff)

    types = ['Gregory_Leibniz', 'Nilakantha', 'Limit']

    print(min(diff_list), types[diff_list.index(min(diff_list))])