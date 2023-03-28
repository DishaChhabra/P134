import csv
import pandas as pd
import matplotlib.pyplot as plt

rows = []
with open("data131.csv" , "r") as f:
    a = csv.reader(f)
    for i in a:
        rows.append(i)

planet_data_rows = rows[1:]
temp_planet_data_rows = list(planet_data_rows)

print(temp_planet_data_rows[0])

temp = temp_planet_data_rows
for i in temp:
    if float(i[5]) > 100:
        temp.remove(i)
    if float(i[6])<150 or float(i[6])>350:
        temp.remove(i)

data = temp
file = open('P134/data134.csv', 'w+', newline ='')
with file:   
    write = csv.writer(file)
    write.writerows(data)





