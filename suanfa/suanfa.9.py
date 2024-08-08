def strList(strlist):
    p = []
    first = strlist[0]

    for j in range(len(first)):
        flag = 0

        for i in range(len(strlist)):
            if first[j] not in strlist[i]:

                flag = 1
                break

        if flag == 0:
            p.append(first[j])

    return p









if __name__ == '__main__':
       l = ["flower", "flow", "flight"]