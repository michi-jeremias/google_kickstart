def is_interesting(integer: int) -> bool:
    interesting = False

    product = 1
    sum = 0

    for d in str(integer):
        product *= int(d)
        sum += int(d)

    q, r = divmod(product, sum)

    if r == 0:
        interesting = True

    return interesting


def solve(A: int, B: int) -> int:

    num_interesting_numbers = 0

    for n in range(A, B+1):
        if is_interesting(n):
            num_interesting_numbers += 1

    return num_interesting_numbers


T = int(input())

for x in range(1, T+1):

    A = int(input())
    B = int(input())

    y = solve(A, B)

    print(f"Case #{x}: {y}", flush=True)


with open("./test_set_2/ts2_input.txt", "r") as infile, open(
    "./test_set_2/ts2_output.txt", "r"
) as outfile:
    data = []
    targets = []

    for line in infile:
        data.append(line.strip("\n"))

    for line in outfile:
        targets.append(line.strip("\n"))

    N = data.pop(0)

    for x, (i, j) in enumerate(zip(data, targets)):
        print(x)
        A, B = i.split(" ")
        y = solve(int(A), int(B))
        res = f"Case #{x+1}: {y}"
        if res != j:
            print(res)
            print(j)
