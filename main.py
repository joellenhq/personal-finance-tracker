import seaborn as sns
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('cosmetics-spendings.csv',encoding='cp1252')
print(dataset.head())
print(dataset.tail())

print(dataset.describe().T)
print(dataset['category'].unique())
print(dataset.shape)

categories = ['gift','face care','additional care','everyday care','make-up']

plt.figure(figsize=(10,6))
plt.title('Product prices')
sns.scatterplot(data=dataset, x='date', y='price')  #,hue='category')
plt.xlabel('Date of purchase')
plt.ylabel('Price of product [zł]')

#plt.show()

print(dataset['date'].unique())
unique_dates = ['30.11.2020','05.01.2021','21.01.2021','18.02.2021','11.06.2021',
'06.07.2021','19.08.2021','20.09.2021','19.11.2021','07.01.2021']

month_price=np.zeros(len(unique_dates))
for i,data in enumerate(unique_dates):
    particular_date = dataset.loc[dataset.date == data]
    for value in particular_date.price:
        month_price[i] = month_price[i] + value
print(month_price)

plt.figure('Overall spendings')
sns.lineplot(x=unique_dates , y=month_price)
plt.xlabel('Date of purchase')
plt.ylabel('Expences [zł]')
plt.show()

category_price=np.zeros(len(categories))
for i,data in enumerate(categories):
    particular_cat = dataset.loc[dataset.category == data]

    for value in particular_cat.price:
        category_price[i] = category_price[i] + value

plt.figure(figsize=(10,6))
plt.title('Categories')
sns.barplot(x=categories, y=category_price)
plt.xlabel('Category')
plt.ylabel('Spendings')
plt.show()




