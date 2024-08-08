def mod2(x):
    s = []
    while x > 0:
        s.append(x % 2)
        x = x // 2

    ans = 0
    for i in range(len(s)):
        ans += s[i]
    return ans


def mod4(x):
    s = []
    while x > 0:
        s.append(x % 4)
        x = x // 4

    ans = 0
    for i in range(len(s)):
        ans += s[i]
    return ans


if __name__ == '__main__':
    # ans = 0
    # for i in range(1, 2025):
    #     if mod4(i) == mod2(i):
    #         ans += 1
    # print(ans)

    # print(mod4(5))
    for i in range(3, -1, -1):
        print(i)

