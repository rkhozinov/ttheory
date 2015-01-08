import math

k1 = 0.1
k2 = 0.9
load_factor = 0.6742

magic1 = 0.114
magic2 = 0.337


def expected_load(load_values):
    return map(lambda load: math.sqrt((load + magic1) - magic2) ** 2, load_values)


def expected_load_by_direction(load_sum, *directions):
    return map(lambda direction: load_sum * direction, directions)


def result_load(_expected_load_by_direction):
    return map(lambda x: x + load_factor * math.sqrt(x), _expected_load_by_direction)


def load_deviation(_result_load, _expected_load_by_direction):
    return map(lambda x, y: (x - y) / y * 100, _result_load, _expected_load_by_direction)


def r(arr):
    return map(lambda _: round(_, 2), arr)


def main(**load):
    _expected_load = expected_load(load.values())
    _expected_load_by_direction = expected_load_by_direction(sum(_expected_load), k1, k2)
    _result_load = result_load(_expected_load_by_direction)
    _load_deviation = load_deviation(_result_load, _expected_load_by_direction)

    print("data: {}\n"
          "expected load: {}\n"
          "expected load by direction: {}\n"
          "result load: {}\n"
          "load deviation: {}".format(load.values(),
                                      r(_expected_load),
                                      r(_expected_load_by_direction),
                                      r(_result_load),
                                      r(_load_deviation)))


if __name__ == "__main__":
    main(yr1=35, yr2=20, yr3=40, yr4=40)

