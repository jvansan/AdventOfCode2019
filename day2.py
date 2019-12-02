from pathlib import Path
from random import choice

def read_file(fname):
    f = Path(fname)
    return [int(x) for x in f.open().read().split(",")]

def fix_program(inputs, noun=12, verb=2):
    copy = inputs.copy()
    copy[1] = noun
    copy[2] = verb
    return copy

def get_opcode(inputs, idx):
    return inputs[idx]

def get_x(inputs, idx):
    return inputs[inputs[idx+1]]

def get_y(inputs, idx):
    return inputs[inputs[idx+2]]

def get_set_idx(inputs, idx):
    return inputs[idx+3]

def run_opcode_1(inputs, idx):
    set_idx = get_set_idx(inputs, idx)
    inputs[set_idx] = get_x(inputs, idx) + get_y(inputs, idx)

def run_opcode_2(inputs, idx):
    set_idx = get_set_idx(inputs, idx)
    inputs[set_idx] = get_x(inputs, idx) * get_y(inputs, idx)

def find_output(inputs, nlim=100, vlim=100, desired=19690720):
    nouns = list(range(nlim))
    verbs = list(range(vlim))

    seen = set()
    while True:
        n = choice(nouns)
        v = choice(verbs)
        if (n,v) in seen:
            continue
        else:
            seen.add((n,v))
        fixed = fix_program(inputs, n, v)
        output = run_program(fixed)
        if output == 19690720:
            return (n,v)

def run_program(inputs):
    # Start at 0
    idx = 0
    while True:
        opcode = get_opcode(inputs, idx)
        if opcode == 99:
            break
        elif opcode == 1:
            run_opcode_1(inputs, idx)
        elif opcode == 2:
            run_opcode_2(inputs, idx)
        else:
            raise Exception("Bad OpCode")
        idx += 4
    return inputs[0]

def test_program():
    assert run_program([1,9,10,3,2,3,11,0,99,30,40,50]) == 3500

def main():
    # Run test
    test_program()
    inputs = read_file("./input/day2.txt")
    program = fix_program(inputs)
    # print(f"{list(program)}")
    print("Part 1:")
    print(f"Final value in idx 0 is : {run_program(program)}")
    print("This returns 100*noun+verb = 1202")

    print("Part 2:")
    noun, verb = find_output(inputs, desired=19690720)
    print(f"The noun={noun} and verb={verb} which return 19690720 give final answert : {100*noun+verb}")

if __name__ == "__main__":
    main()