
if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            k = 1
            while i - k >= 0 or j - k >= 0 or i + k < n or j + k < m:
                if i - k >= 0 and j - k >= 0 and a[i][j] == a[i - k][j - k]:
                    ans += 1
                if i - k >= 0 and j + k < m and a[i][j] == a[i - k][j + k]:
                    ans += 1
                if i + k < n and j - k >= 0 and a[i][j] == a[i + k][j - k]:
                    ans += 1
                if i + k < n and j + k < m and a[i][j] == a[i + k][j + k]:
                    ans += 1
                k += 1

    print(ans)
