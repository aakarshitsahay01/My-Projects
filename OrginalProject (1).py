import urllib
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
df = pd.read_csv('WHO-COVID-19-global-data (1).csv')
df
df.shape
df.columns
df.head(10)
df.tail()
df[df.isna().any(axis=1)]
df['Country'].unique()
df['Country']
df_india = df[df.Country == 'India']
df_india
new_cases = df_india[df_india.New_cases > 1000]
new_deaths = df_india[df_india.New_deaths > 1000]
tot_deaths = df_india['New_deaths'].sum()
tot_cases = df_india['New_cases'].sum()
df_india.columns
df5 = df_india.iloc[0:100]
df5 = df5.loc[df.New_deaths > 0, ['Date_reported','New_cases','New_deaths']]
x = df5.Date_reported
y = df5.New_cases
z = df5.New_deaths
plt.plot(x,y,label = 'New Cases' , color = 'b')
plt.plot(x,z,label = 'New Deaths' , color = 'r')
plt.title('India Covid Situation')
plt.xlabel('Date Reported')
plt.ylabel('New Cases and Deaths')
plt.legend()
plt.show()