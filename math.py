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


def get_binary_info(base10number):
    python_binary = bin(base10number)
    string_binary = python_binary[2:]
    string_len = len(string_binary)
    if string_len < 5:
        pad_binary = ('0' * (4 - string_len)) + string_binary
    elif string_len < 9:
        pad_binary = ('0' * (8 - string_len)) + string_binary
    elif string_len < 17:
        pad_binary = ('0' * (16 - string_len)) + string_binary
    elif string_len < 33:
        pad_binary = ('0' * (32 - string_len)) + string_binary
    elif string_len < 65:
        pad_binary = ('0' * (64 - string_len)) + string_binary
    else:
        pad_binary = 'Over 64 bits not coded'
    print('Base 10 Number:', base10number)
    print('Binary:', string_binary)
    print('Bits:', string_len)
    print('Formatted:', pad_binary)
    print('Formatted Bits:', len(pad_binary))
    print('Formatted Bytes', int(len(pad_binary) / 8))
