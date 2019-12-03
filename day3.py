from pathlib import Path

def read_input(fname):
    fil = Path(fname)
    with fil.open() as f:
        p = f.readline().strip().split(",")
        q = f.readline().strip().split(",")
    return p, q

def get_direction(inp):
    d = inp[0]
    m = int(inp[1:])
    return d, m

def get_path(vect):
    # x, y coordinates starting at 0,0
    path = [(0,0)]
    for v in vect:
        l = path[-1] # last point
        d, m = get_direction(v)
        if d == "L":
            path += [(l[0]-i, l[1]) for i in range(1,m+1)]
        elif d == "D":
            path += [(l[0], l[1]-i) for i in range(1,m+1)]
        elif d == "R":
            path += [(l[0]+i, l[1]) for i in range(1,m+1)]
        elif d == "U":
            path += [(l[0], l[1]+i) for i in range(1,m+1)]
    return path

def get_intersections(u, v):
    u, v = set(u), set(v)
    return u.intersection(v) - {(0,0)} # Remove origin

def manhattan_distance(p, q):
    assert len(p) == len(q)
    return sum(abs(x-y) for x,y in zip(p, q))

def step_distance(path, intersect):
    return path.index(intersect)

def run_manhattan_calc(p ,q):
    u, v = get_path(p), get_path(q)
    intersects = get_intersections(u, v)
    return min(manhattan_distance((0,0), i) for i in intersects)

def run_steps_calc(p, q):
    u, v = get_path(p), get_path(q)
    intersects = get_intersections(u, v)
    u_dist = [step_distance(u, i) for i in intersects]
    v_dist = [step_distance(v, i) for i in intersects]
    distances = map(sum, zip(u_dist, v_dist))
    return min(distances)

def run_manhattan_tests():
    assert run_manhattan_calc(
        ['R75','D30','R83','U83','L12','D49','R71','U7','L72'],
        ['U62','R66','U55','R34','D71','R55','D58','R83']
    ) == 159
    assert run_manhattan_calc(
        ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],
        ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
    ) == 135

def run_steps_test():
    assert run_steps_calc(
        ['R75','D30','R83','U83','L12','D49','R71','U7','L72'],
        ['U62','R66','U55','R34','D71','R55','D58','R83']
    ) == 610
    assert run_steps_calc(
        ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],
        ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
    ) == 410

def main():
    # Tests 1
    run_manhattan_tests()
    print("Part 1:")
    p, q = read_input("input/day3.txt")
    res = run_manhattan_calc(p,q)
    print(f"The Manhattan Distance is {res}\n")

    # Tests 2
    run_steps_test()
    print("Part 2:")
    res1 = run_steps_calc(p, q)
    print(f"The minimum number of combined steps is {res1}")

if __name__ == "__main__":
    main()