from tqdm import trange


def is_even(integer):
    # Returns True if integer given is even, else it will return False
    if isinstance(integer, int):
        # Checks if integer is divisible by 2
        if integer % 2 == 0:
            return True
        else:
            return False
    else:
        raise TypeError('integer must be an integer')


def is_odd(integer):
    # Returns True if integer given is odd, else it will return False
    return not is_even(integer)


def get_factors(number, progess_bar=False):
    # Returns te factors of a number.
    # Making progress_bar=True will make a progress bar to see how far along it is at calculating the factors using tqdm
    factors = []
    if progess_bar:
        for x in trange(1, int(number + 1 / 2 + 3)):
            if number % x == 0:
                factors.append(x)
        return factors
    else:
        for x in range(1, int(number + 1 / 2 + 3)):
            if number % x == 0:
                factors.append(x)
        return factors


def is_prime(number, progress_bar=False):
    # Returns True if number given is prime, else it will return False
    # Making progress_bar=True will make a progress bar to see how far along it is at calculating the factors using tqdm
    if not isinstance(number, int):
        raise TypeError('number must be an integer')
    elif number < 1:
        raise ValueError('number must be at least 2')
    factors = []
    if is_even(number) and number > 2:
        return False
    elif number == 1:
        return False
    else:
        if progress_bar:
            for x in trange(1, int(number + 1 / 2 + 3)):
                if number % x == 0:
                    factors.append(x)
                if len(factors) > 3:
                    return False
            return True
        else:
            for x in range(1, int(number + 1 / 2 + 3)):
                if number % x == 0:
                    factors.append(x)
                if len(factors) > 3:
                    return False
            return True


def help_is_prime(factors):
    # If you have already calculated the factors and saved it in a variable,
    # you can put the give it to this function so you don't have to do unnecessary calculation
    if len(factors) <= 3:
        return True
    else:
        return False


def is_semiprime(number, progress_bar=False):
    # Returns True if number given is prime, else it will return False
    # Making progress_bar=True will make a progress bar to see how far along it is at calculating the factors using tqdm
    factors = get_factors(number, progess_bar=progress_bar)
    # A semiprime is a natural number that is the product of two prime numbers.
    # You can argue that 2 is prime,
    # but I'm not counting it because it would dramatically increase the number of semiprimes
    if len(factors) > 2 and factors[1] != 2:
        return True
    else:
        return False


def help_is_semiprime(factors):
    # If you have already calculated the factors and saved it in a variable,
    # you can put the give it to this function so you don't have to do unnecessary calculation
    if len(factors) > 2 and factors[1] != 2:
        return True
    else:
        return False


def concatenate(list_of_numbers):
    # Returns a number that is the combination of putting the numbers in a list next to each other
    string = ''
    if isinstance(list_of_numbers, list):
        pass
    else:
        raise TypeError(
            'list_of_numbers must be a list. If you are using a numpy array, you can use list(array_of_numbers_variable)')
    for x in list_of_numbers:
        if isinstance(x, int):
            string += str(x)
        else:
            raise TypeError('All values in list_of_numbers must be integers')
    return int(string)


def generate_primes(max):
    # Generates primes from 1 to max (inclusive)
    for x in range(1, max + 1, 2):
        if is_prime(x):
            yield x


def list_primes(max, progess_bar=False):
    # Returns a list of primes from 1 to max (inclusive)
    # Making progress_bar=True will make a progress bar to see how far along it is at calculating the factors using tqdm
    primes = []
    if progess_bar:
        for x in trange(1, max + 1, 2, desc='Generating list of primes'):
            if is_prime(x):
                primes.append(x)
    else:
        for x in range(1, max + 1, 2):
            if is_prime(x):
                primes.append(x)
    return primes


class fibonacci(object):
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
