def calculate(P,N,R):

    total = N

    day = 0
    day_num = N
    while total <= P:
        day += 1

        day_num *= R
        total += day_num

    print(str(day))

    num = []
    for i in range(3):
        num.append(int(input()))

if __name__ == '__main__':


    pass
