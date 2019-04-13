# Different ways of generating pi

from tqdm import trange
import math
import time


def Gregory_Leibniz(max_num):
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
    gl_var = Gregory_Leibniz()
    time1 = time.time()
    n_var = Nilakantha()
    time2 = time.time()
    l_var = limit()
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