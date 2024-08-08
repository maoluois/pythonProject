# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
file_name = "计算机科学与技术学院-研究生欠费.xlsx"

df = pd.read_excel(file_name)
# print(df)
# print(df.head())  头5个  tail 后5个
# print(df["学院"])
# print(df["姓名"])
# print(df.at[0,"学号"])
# print(df.index)
# print(df.columns)
# print(df.dtypes)
# print(df.info())
# print(df[["本年应收","未交金额"]])
test_number = np.arange(0,113)
# print(test_number)
# df["test_number"] = test_number
# print(df)
# df["test_number"].count()
# df["test_number"].mean()
# df["test_number"].sum()
# print(df["test_number"].sum())

df.to_excel("计算机科学与技术学院-研究生欠费2.xlsx",sheet_name="计算机科学与技术学院")
