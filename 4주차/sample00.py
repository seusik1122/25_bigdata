import pandas as pd

covid_file_name = 'C:/Users/kim/Desktop/공부/학교/2-2/빅데이터/25_bigdata/4주차/owid-covid-data.csv'
raw_pd = pd.read_csv(covid_file_name, sep=',')

print(raw_pd)
#print(dir(raw_pd))

print('*'*50)
print(raw_pd.info())

print('*'*50)
print(raw_pd.head())