
def huiWen(string):

    b = len(string)
    left = 0
    right = b - 1



    flag = 1


    while left <= right:
        if string[left] == string[right]:
            left = left + 1
            right = right + 1
        else:
            flag = 0
            break

        if flag == 1:
            return 'yes'
        else:
            return 'no'



    if flag == 1:
        return 'yes'
    else:
        return 'no'



def huWen2(string):
    b = len(string)
    i = 0
    flag = 1
    while i < b//2:

        if string[i] == string[b - i - 1]:
            i += 1
        else:
            flag = 0
            break

    if flag == 1:
        return 'yes'
    else:
        return 'no'



def huWen3(string):
    if string == string[::-1]:

        return 'yes'
    else:
        return 'no'



if __name__ == '__main__':
    b = input()
    a = huiWen(b)
    print(a)




