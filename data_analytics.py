import matplotlib.pyplot as plt
import pandas as pd
import os

path = os.chdir("D:\\Новая папка (2)")
path = os.getcwd()
file = '\AUTO RIA.xlsx'

xl = pd.read_excel(path+file)
small = []
mid = []
large = []
another = []

xl["Цена"] = pd.to_numeric(xl["Цена"], errors='coerce', downcast='float')
xl["Объем"] = pd.to_numeric(xl["Объем"], errors='coerce', downcast='float').round(1)
xl["Пробег"] = pd.to_numeric(xl["Пробег"], errors='coerce', downcast='float').fillna(0)

xl["Объем"] = xl["Объем"].astype(str)
xl["Пробег"] = xl["Пробег"].astype(int)

result_value = xl["Объем"].value_counts().drop_duplicates().drop('nan')

result_miliage = xl["Пробег"].value_counts().drop(1)

fig, axes = plt.subplots(2, 1)
bar1 = result_value[:40].plot.bar(title="Кол-во авто по объему двигателя до 3k $", ax=axes[0])
bar2 = result_miliage[:40].plot.bar(title="Кол-во авто по пробегу (в тыс.км)", ax=axes[1])
plt.show()
