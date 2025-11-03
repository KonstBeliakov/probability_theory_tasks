import numpy as np
from numpy.random.mtrand import random_sample
from math import log

rng = np.random.default_rng() # set up the random number generator


def randbits(size):
    """
    Return the numpy array of size `size`, filled with random bits.
    Size can be an integer or a tuple of integers.
    """
    return rng.integers(low=0, high=1, endpoint=True, size=size, dtype=np.uint8)

def uniform(shape: tuple) -> list[float]:
    """
    :param shape: shape of a generating array
    :return: random np array filled with values between 0 and 1
    """
    size = np.prod(shape)
    lst = np.zeros(size)
    for n in range(size):
        t = 0.5
        rv = 0.0
        for i in randbits(100):
            if i:
                rv += t
            t /= 2
        lst[n] = rv
    return lst.reshape(shape)

def randint(shape: tuple):
    """
    :param shape: shape of returning array
    :return: numpy array filled with random integers
    """
    size = np.prod(shape)
    lst = np.zeros(size)
    for n in range(size):
        rv = 0
        t = 1
        for i in randbits(100):
            if i:
                rv += t
            t *= 2
        lst[n] = rv
    return lst.reshape(shape)

def exponential_rv(rate: int, size: int) -> list[float]:
    return [-(1/rate)*log(i) for i in uniform(size)]

def poison_process(rate: int, size: int) -> list[float]:
    return np.cumsum(exponential_rv(rate, size))


if __name__ == '__main__':
    print(randbits(5))
    print(uniform((2, 3)))
    print(randint(5))
    print(exponential_rv(1, 5))
    print(poison_process(1, 5))
