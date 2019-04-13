def gen_fibonacci_steps(steps):
    # Generates the first {steps} fibonacci numbers
    one_ago = 1
    two_ago = 1
    now = one_ago + two_ago
    yield 1
    yield 1
    for _ in range(steps - 2):
        yield now
        two_ago = one_ago
        one_ago = now
        now = one_ago + two_ago


def gen_fibonacci_max(max):
    # Generates all the fibonacci numbers up to max (uninclusive)
    one_ago = 1
    two_ago = 1
    now = one_ago + two_ago
    yield 1
    yield 1
    while now < max:
        yield now
        two_ago = one_ago
        one_ago = now
        now = one_ago + two_ago


def list_fibonacci_steps(steps):
    # Generates a list of the first {steps} fibonacci numbers
    return_list = []
    for num in gen_fibonacci_steps(steps):
        return_list.append(num)
    return return_list


def list_fibonacci_max(max):
    # Returns a list of  all the fibonacci numbers up to max (uninclusive)
    return_list = []
    for num in gen_fibonacci_steps(max):
        return_list.append(num)
    return return_list


def custom_gen_fibonacci_steps(num1, num2, steps):
    # Generates numbers with fibonacci rules, but with any numbers you want instead of 1 and 2
    # It will generate the first {steps} numbers
    one_ago = num2
    two_ago = num1
    now = one_ago + two_ago
    yield two_ago
    yield one_ago
    for _ in range(steps - 2):
        yield now
        two_ago = one_ago
        one_ago = now
        now = one_ago + two_ago


def custom_gen_fibonacci_max(num1, num2, max_num):
    # Generates numbers with fibonacci rules, but with any numbers you want instead of 1 and 2
    # It will generate the numbers up to max_num (uninclusive)
    one_ago = num2
    two_ago = num1
    now = one_ago + two_ago
    yield two_ago
    yield one_ago
    while now < max_num:
        yield now
        two_ago = one_ago
        one_ago = now
        now = one_ago + two_ago


def custom_gen_fibonacci_steps_max(num1, num2, steps, max):
    # Generates numbers with fibonacci rules, but with any numbers you want instead of 1 and 2
    # It will generate the first {steps} numbers or until hitting max_num
    one_ago = num2
    two_ago = num1
    now = one_ago + two_ago
    yield two_ago
    yield one_ago
    for _ in range(steps - 2):
        if now > max:
            break
        yield now
        two_ago = one_ago
        one_ago = now
        now = one_ago + two_ago


def custom_list_fibonacci_steps(num1, num2, steps):
    # Returns a list of numbers with fibonacci rules, but with any numbers you want instead of 1 and 2
    # It will generate the first {steps} numbers
    return_list = []
    for num in custom_gen_fibonacci_steps(num1, num2, steps):
        return_list.append(num)
    return return_list


def custom_list_fibonacci_max(num1, num2, max):
    # Returns a list of numbers with fibonacci rules, but with any numbers you want instead of 1 and 2
    # It will generate the numbers up to max_num (uninclusive)
    return_list = []
    for num in custom_gen_fibonacci_max(num1, num2, max):
        return_list.append(num)
    return return_list


def custom_list_fibonacci_steps_max(num1, num2, steps, max):
    # Returns a list of numbers with fibonacci rules, but with any numbers you want instead of 1 and 2
    # It will generate the first {steps} numbers or until hitting max_num
    return_list = []
    for num in custom_gen_fibonacci_steps_max(num1, num2, steps, max):
        return_list.append(num)
    return return_list


def list_lucas_numbers_steps(steps):
    # Returns a list of the first {steps} Lucas numbers
    return custom_list_fibonacci_steps(2, 1, steps)


def list_lucas_numbers_max(max):
    # Returns a list of all the Lucas numbers up to max (uninclusive)
    return custom_list_fibonacci_max(2, 1, max)


def list_lucas_numbers_steps_max(steps, max):
    # Returns a list of Lucas numbers
    # It will generate the first {steps} numbers or until hitting max_num
    return custom_list_fibonacci_steps_max(2, 1, steps, max)


def gen_lucas_numbers_steps(steps):
    # Generates the first {steps} Lucas numbers
    return custom_gen_fibonacci_steps(2, 1, steps)


def gen_lucas_numbers_max(max):
    # Generates all the Lucas numbers up to max (uninclusive)
    return custom_gen_fibonacci_max(2, 1, max)


def gen_lucas_numbers_steps_max(steps, max):
    # Generates Lucas number
    # It will generate the first {steps} numbers or until hitting max_num
    return custom_gen_fibonacci_steps_max(2, 1, steps, max)
