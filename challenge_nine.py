T = int(input())

for x in range(1, T+1):

    I = str(input())

    first_digit = I[0]

    found = False

    for i in range(1, int(first_digit)):
        y = int(str(i)+I)
        if y % 9 == 0:
            found = True
            break

    if not found:
        # traverse array from end to beginning
        for j in range(len(I)-1, -1, -1):
            I_copy = I
            for i in range(10):
                I_copy = I[:j] + str(i) + I[:j+2]

                y = int(I+str(i))
                if y % 9 == 0:
                    found = True
                    break

    print(f"Case {x}: {y}")

for i in range(len(I)-1, -1, -1):
    print(i)


I = "5"

I = "33"

I = "12121"

I = "9"