from math import factorial as fact

__author__ = 'rkhozinov'

A = 0.53
n = 9


def bernoulli_distribution(n, k, a):
    return [round((fact(n) * (a ** k * (1 - a) ** (n - k))) / (fact(k) * fact(n - k)), 5) for k in xrange(k + 1)]


if __name__ == "__main__":
    a = A / (1 + A)
    print a
    print bernoulli_distribution(n, n, a)


