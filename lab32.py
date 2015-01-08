import math

__author__ = 'rkhozinov'

order_time = 3
load = 0.4
channels = 3


def main(desired_orders):
    u = 1 / float(order_time)
    p = order_time * float(load)
    print p
    _ = [p ** x / math.factorial(x) for x in xrange(channels + 1)]
    print _
    p_0 = 1 / sum(_)
    p_err = _[-1] * p_0
    p_srv = 1 - p_err

    A = p_srv * load

    print ("p0: {:.2f}%\n"
           "errors: {:.2f}%\n"
           "serviced: {:.2f}%\n"
           "absolute bandwidth: {:.3f} orders per hour".format(p_0 * 100, p_err * 100, p_srv * 100, A))

if __name__ == "__main__":
    main(desired_orders=90)


