import math

__author__ = 'rkhozinov'

h = 35
limit = 2

channels = 5
order_time = 3
tobc = 60
u = tobc / order_time
p = h * order_time / float(tobc)

p0 = u / float(h + u)

pfree = [(p ** x) / math.factorial(x) * p0 for x in range(channels + 1)]
perr = (p ** channels + limit) * p0 / ((channels ** limit) * math.factorial(channels))
if __name__ == "__main__":
    print u
    print p
    print p0
    print pfree
    print perr



