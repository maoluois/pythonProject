import os
def deal_excel(filename,save_name):

    print(filename)
    pass


if __name__ == '__main__':

    dir = "C:/Users/lmz/PycharmProjects/pythonProject/excel python"
    filenames = os.listdir(dir) # 获取所有的文件名字
    for file in filenames:
        if file.endswith(".xlsx"):
            # print(file)
            file_path = os.path.join(dir,file) # 获取完整路径
            deal_excel(file_path,file_path+"_save")





