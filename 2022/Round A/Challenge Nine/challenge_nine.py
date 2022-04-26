def find_target_digit(I, modulo):
    # target_digit = 0
    sum_digits = sum([int(d) for d in I])

    # return modulo - (sum_digits % modulo)

    for target_digit in range(modulo):
        if (sum_digits + target_digit) % modulo == 0:
            return target_digit


def find_y(I):
    I = str(I)
    target_digit = find_target_digit(I, 9)

    if target_digit != 0:
        if len(I) > 1:
            for j in range(len(I)):
                if int(I[j]) > target_digit:
                    y = int(I[:j] + str(target_digit) + I[j:])
                    return y
            y = int(I + str(target_digit))
            return y
        else:
            if int(I[0]) > target_digit:
                y = int(str(target_digit) + I)
                return y
            else:
                y = int(I + str(target_digit))
                return y

    else:
        y = int(I[0] + str(target_digit) + I[1:])
        return y


T = int(input())

for x in range(1, T + 1):

    I = str(input())

    y = find_y(I)
    print(f"Case {x}: {y}", flush=True)


with open("./test_set_1/ts1_input.txt", "r") as infile, open(
    "./test_set_1/ts1_output.txt", "r"
) as outfile:
    data = []
    targets = []

    for line in infile:
        data.append(line.strip("\n"))

    for line in outfile:
        targets.append(line.strip("\n"))

    N = data.pop(0)


for k, v in test_I.items():
    res = find_y(k)
    if res != int(v):
        print(f"I: {k}, out: {res}, expected: {v}")
