import matplotlib.pyplot as plt
import pandas as pd
if __name__ == '__main__':
    # df = pd.read_csv("C:/Users/lmz/PycharmProjects/pythonProject/excel python/lesson_3/gdp.csv",encoding="gbk")
    # print(df)
    # a = df.pivot(index="year",columns="country",values="gdppc")
    # print(a)
    ab = pd.read_csv("C:/Users/lmz/PycharmProjects/pythonProject/excel python/lesson_3/population_total.csv",encoding="gbk")
    # print(ab)
    ab.dropna(inplace=True)
    # print(ab)
    ab = ab.pivot(index="year",columns="country",values="population")
    ab_pivot = ab[['United States', 'India', 'China',
                         'Indonesia', 'Brazil']]
    # print(ab_pivot)
    ab_pivot.plot(kind="line",xlabel='year',ylabel='population',title='Population(1955-2020)',
                  figsize=(8,4))
    print(ab_pivot)