#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'/mnt/c/Users/HP/Desktop/STUFF/DATA/Kaggle datasets/Africa_population.csv')
#data = pd.DataFrame(df, columns=['Season'])
#print(df)
plt.plot(df['Country'], df['2020'])
plt.show()
