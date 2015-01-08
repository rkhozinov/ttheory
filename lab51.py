__author__ = 'rkhozinov'

n_digit = 6
load_factor = 0.1
lines_load_factor = 0.0023
services_load_factor = 0.05
load_time = 16
factor = load_factor * load_time

load = {"individual": [2000, 0.022, 0.030, 0],
        "business": [3000, 0.07, 0.03, 1],
        "sleep": [2000, 0.07, 0.03, 1],
        "local": [150, 0.2, 0.27, 0],
        "inter": [15, 0.65, 0.65, 0],
        "district": [40, 0.6, 0.6, 1],
        "sl": [40, 0.15, 0.15, 1],
        "fax": [50, 0.15, 0.15, 1],
        "type_2bd": [4, 0.5, 21, 1],
        "type_30bd": [4, 0.5, 21, 1]}


def morning_load(_load):
    _ = 0
    _filter = [x for x in _load.items() if x[1][3]]
    for x in load.items():
        tmp = x[1][0] * x[1][1]
        if x in _filter:
            _ += round(tmp + tmp / factor, 2)
        else:
            _ += round(tmp, 2)
    return _


def night_load(_load):
    _ = 0
    _filter = [x for x in _load.items() if not x[1][3]]
    for x in load.items():
        tmp = x[1][0] * x[1][2]
        if x in _filter:
            _ += round(tmp + tmp / factor, 2)
        else:
            _ += round(tmp, 2)
    return _


def leased_lines_load(_load):
    return sum(map(lambda x: x[1][0] * lines_load_factor, _load.items()))


def main():
    _morning_load = morning_load(load)
    _night_load = night_load(load)
    _lines_load = leased_lines_load(load)
    _services_load = _morning_load * services_load_factor
    _common_load = _morning_load + _lines_load + _services_load

    print("morning load: {} Erl\n"
          "night load: {} Erl\n"
          "leased lines load: {} Erl\n"
          "services load: {} Erl\n"
          "common load: {} Erl".format(_morning_load,
                                       _night_load,
                                       _lines_load,
                                       _services_load,
                                       _common_load))

if __name__ == "__main__":
    main()

