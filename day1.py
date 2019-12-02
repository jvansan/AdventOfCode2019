import math
from pathlib import Path

def read_file(fname):
    f = Path(fname)
    with open(f) as inp:
        data = inp.readlines()
    
    return (int(x) for x in data)

def calc_fuel(x):
    return math.floor(x/3.)-2

def test_calc_fuel():
    assert calc_fuel(12) == 2
    assert calc_fuel(14) == 2
    assert calc_fuel(1969) == 654
    assert calc_fuel(100756) == 33583

def main():
    # Run test
    test_calc_fuel()
    inputs = read_file("./input/day1.txt")
    fuel = map(calc_fuel, inputs)
    print(f"Total fuel needed is : {sum(fuel)}")

if __name__ == "__main__":
    main()