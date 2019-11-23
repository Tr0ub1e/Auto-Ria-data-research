import matplotlib.pyplot as plt
import pandas as pd
import os

path = os.chdir("D:\\Новая папка (2)")
path = os.getcwd()
file = '\AUTO RIA.xlsx'

xl = pd.read_excel(path+file)


xl["Цена"] = pd.to_numeric(xl["Цена"], errors='coerce', downcast='float').fillna(0)
xl["Объем"] = pd.to_numeric(xl["Объем"], errors='coerce', downcast='float').round(1)
xl["Пробег"] = pd.to_numeric(xl["Пробег"], errors='coerce', downcast='float').fillna(0)

xl["Объем"] = xl["Объем"].astype(str)
xl["Пробег"] = xl["Пробег"].astype(int)
xl["Цена"] = xl["Цена"].astype(int)

sorted_cost = {
                "<0.5k": 0, ">0.5k and <1k": 0,
                ">1k and <1.5k": 0, ">1.5K and <2k":0,
                ">2k and <2.5k":0, ">2.5k and <3k":0
                }

sorted_miliage = {
                "<50km": 0, ">50 and <100km": 0, ">100 and <150km": 0,
                ">150 and <200km": 0, ">200 and <250km": 0, ">250 and <300km": 0,
                ">300km": 0
                }

sorted_value = {
                "1.1": 0, "1.2": 0, "1.3": 0, "1.4": 0, "1.5": 0, "1.6": 0,
                "1.7": 0, "1.8": 0, "1.9": 0, "2.0": 0, "NaN": 0
                }

for i in xl["Цена"]:

    if i > 0 and i <= 500:
        sorted_cost["<0.5k"] += 1

    elif i > 500 and i <= 1000:
        sorted_cost[">0.5k and <1k"] += 1

    elif i > 1000 and i <= 1500:
        sorted_cost[">1k and <1.5k"] += 1

    elif i > 1500 and i <= 2000:
        sorted_cost[">1.5K and <2k"] += 1

    elif i > 2000 and i <= 2500:
        sorted_cost[">2k and <2.5k"] += 1

    else:
        sorted_cost[">2.5k and <3k"] += 1


for i in xl["Пробег"]:

    if i > 0 and i <= 50:
        sorted_miliage["<50km"] += 1

    elif i > 50 and i <= 100:
        sorted_miliage[">50 and <100km"] += 1

    elif i > 100 and i <= 150:
        sorted_miliage[">100 and <150km"] += 1

    elif i > 150 and i <= 200:
        sorted_miliage[">150 and <200km"] += 1

    elif i > 200 and i <= 250:
        sorted_miliage[">200 and <250km"] += 1

    elif i > 250 and i <= 300:
        sorted_miliage[">250 and <300km"] += 1
    else:
        sorted_miliage[">300km"] += 1


for i in xl["Объем"]:

    if i == "1.1":
        sorted_value["1.1"] += 1

    elif i == "1.2":
        sorted_value["1.2"] += 1

    elif i == "1.3":
        sorted_value["1.3"] += 1

    elif i == "1.4":
        sorted_value["1.4"] += 1

    elif i == "1.5":
        sorted_value["1.5"] += 1

    elif i == "1.6":
        sorted_value["1.6"] += 1

    elif i == "1.7":
        sorted_value["1.7"] += 1

    elif i == "1.8":
        sorted_value["1.8"] += 1

    elif i == "1.9":
        sorted_value["1.9"] += 1

    elif i == "2.0":
        sorted_value["2.0"]

    else:
        sorted_value["NaN"] += 1

result_cost = pd.Series(sorted_cost, index=sorted_cost.keys())
result_value = pd.Series(sorted_value,index=sorted_value.keys())
result_miliage = pd.Series(sorted_miliage, index=sorted_miliage.keys())


fig, axes = plt.subplots(2, 2)
bar1 = result_value.plot.bar(title="Кол-во авто по объему двигателя до 3k $", ax=axes[0,0])
bar2 = result_miliage.plot.barh(title="Кол-во авто по пробегу (в тыс.км)", ax=axes[1,0])
bar3 = result_cost.plot.pie(title="Цена на авто", ax=axes[0, 1])
plt.show()
