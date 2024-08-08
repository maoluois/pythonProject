import math

if __name__ == '__main__':
    # print((math.comb(10000,2) * pow(9, 9998)) % (pow(10,9) + 7))
    ans = 0
    for i in range(1, 10001):
        ans += math.comb(10000, i) * 2 * pow((10000 - i), 7)
    ans = ans % (pow(10,9) + 7)
    print(ans)
