
if __name__ == '__main__':

    m = [[1,2,3],[7,8,9],[2,1,5]]

    he = sum(list(map(lambda x:sum(x),m)))

    print(he)


