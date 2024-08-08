

class jisuanqi():

    def __init__(self):
        # 开启窗口，类的执行过程

        n1 = int(input('请输入一个数：\n'))
        n2 = int(input('请输入第二个数：\n'))
        fuhao = int(input('请选择算法，1：加法，2：减法，3：乘法，4：除法\n'))

        if fuhao == 1:
            he = self.jia(n1,n2)

            print(he)
        if fuhao == 2:
            cha = self.jian(n1,n2)
            print(cha)

        if fuhao == 3:
            ji = self.cheng(n1,n2)
            print(ji)

        if fuhao == 4:
            shang = self.chu(n1,n2)
            print(shang)

    def jia(self,n1,n2):
        he = n1 + n2
        return he

    def jian(self,n1,n2):
        cha= n1 - n2
        return cha

    def cheng(self,n1,n2):
        ji = n1*n2
        return ji

    def chu(self,n1,n2):
        if n2 != 0:
            shang = n1/n2
            return shang



if __name__ == '__main__':
    jisuanqi()