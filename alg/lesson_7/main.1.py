def S3(list):
    p = []
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            y = abs(list[i] - list[j])
            x = j - i
            s = x * y
            p.append(s)

    return max(p)

if __name__ == '__main__':
    a = [1, 12, 16, 3, 8, 10, 7]
    print(S3(a))