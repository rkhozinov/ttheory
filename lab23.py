__author__ = 'rkhozinov'
from math import factorial as fact
from math import e


streams = 2
h1 = 10
h2 = 12
order_time = 0.12


def puasson_distribution(h, t, k):
    return ((h * t) ** k) / fact(k) * (e ** (-h * t))


if __name__ == "__main__":
    print puasson_distribution(h=h1 + h2, t=order_time, k=streams)


