if __name__ == '__main__':
    T = int(input(""))
    while T > 0:
        a = list(map(str, input().split(" ")))
        # print(a[0])
        a[0] = list(map(int, str(a[0]).split("-")))
        a[1] = list(map(int, str(a[1]).split(":")))
        a[2] = int(a[2])
        # print(a)
        mi = 0
        for i in range(1970, a[0][0] + 1):
            if i % 4 == 0:
                mi += 366 * 24 * 60
            else:
                mi += 365 * 24 * 60

        for j in range(1, a[0][1]):
            if j == 1 or 3 or 5 or 7 or 9 or 10 or 12:
                mi += 31 * 24 * 60
            else:
                mi += 30 * 24 * 60
        mi += a[0][2] * 24 * 60
        mi += a[1][0] * 60
        mi += a[1][1]

        mi = mi % a[2]
        a[1][1] -= mi

        print(f"{a[0][0]:04d}-{a[0][1]:02d}-0{a[0][2]:02d} {a[1][0]:02d}:{a[1][1]:02d}:00")
        # if (a[1][1] - mi) >= 0:
        #     a[1][1] -= mi
        # else:
        #     if a[1][0]  >= 0:
        #         a[1][0] -= 1
        #         a[1][1] += 60 - mi

        T -= 1

