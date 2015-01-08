__author__ = 'rkhozinov'
order_time = 2

system_parameters = ((0.25, 22.5),
                     (0.47, 42.4),
                     (0.65, 58.8),
                     (0.79, 71.5),
                     (0.90, 80.1),
                     (0.95, 85.3))


def count_optimal_params(desired_orders):
    desired_orders = desired_orders / 100.0
    return [x for x in system_parameters if x[0] >= desired_orders]


def main(desired_orders):
    print ("desired orders: {}\n".format(desired_orders))
    service_load = 60 / order_time
    load = desired_orders / service_load
    p0 = service_load / float(desired_orders + service_load)

    for x in count_optimal_params(desired_orders):
        channels = system_parameters.index(x) + 1
        print ("channels: {}\n"
               "orders: {}\n"
               "loaded channels: {} \n\n".format(channels,
                                                 x[1],
                                                 x[1] / service_load))


if __name__ == "__main__":
    main(desired_orders=90)

