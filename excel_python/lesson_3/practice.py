# -*- coding: utf-8 -*-
import pandas as pd
if __name__ == '__main__':

    file_name = "计算机科学与技术学院-研究生欠费.xlsx"
    df = pd.read_excel(file_name)
    item = df["未交金额"]
    result = item/1000
    df["result"] = result
    print(df)