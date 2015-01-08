import math

__author__ = 'rkhozinov'

orders = 280
order_time = 90

dx = mx = h = c1 = orders

ht = (orders * order_time) / 3600


def puasson_distribution(ht, k):
    return (ht ** k) / math.factorial(k) * (math.e ** -ht)


if __name__ == "__main__":
    print puasson_distribution(ht=7, k=5)
    print puasson_distribution(ht=7, k=6)


