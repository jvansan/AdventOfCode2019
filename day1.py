import math
from pathlib import Path

def read_file(fname):
    f = Path(fname)
    with open(f) as inp:
        data = inp.readlines()
    
    return (int(x) for x in data)

def calc_fuel(x):
    return math.floor(x/3.)-2

def calc_fuel_with_fuel(x):
    fuel = calc_fuel(x)

    x = fuel
    while True:
        y = calc_fuel(x)
        if y > 0:
            x = y
            fuel += y
        else:
            break
    return fuel

def test_calc_fuel():
    assert calc_fuel(12) == 2
    assert calc_fuel(14) == 2
    assert calc_fuel(1969) == 654
    assert calc_fuel(100756) == 33583

def main():
    # Run test
    test_calc_fuel()
    inputs = list(read_file("./input/day1.txt"))
    fuel = map(calc_fuel, inputs)
    print("Part 1:")
    print(f"Total fuel needed is : {sum(fuel)}")

    print("Part 2:")
    all_fuel = map(calc_fuel_with_fuel, inputs)
    print(f"Total fuel needed (with fuel of fuel) is : {sum(all_fuel)}")


if __name__ == "__main__":
    main()