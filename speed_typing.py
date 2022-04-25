T = int(input())

for x in range(1, T+1):

    I = input()
    P = input()

    y = len(P) - len(I)

    p_idx = 0

    for char in I:
        p_idx = P.find(char, p_idx) + 1

        if not p_idx:
            y = "IMPOSSIBLE"
            break

    print(f"Case #{x}: {y}")
