import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import numpy as np
import datetime
from datetime import date
from sklearn import linear_model


def count_linear_model(x, y):

    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=0)
    linear_model1 = linear_model.LinearRegression()
    linear_model1.fit(x_train, y_train)
    acc = linear_model1.score(x_test, y_test)
    print(acc)
    print('Coefficient: \n', linear_model1.coef_)
    print("Intercept: \n", linear_model1.intercept_)
    return linear_model1

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
#plt.show()

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
#plt.show()

#change column date type String to type datetime
dataset['date'] = pd.to_datetime(dataset['date'])
print(dataset['date'])
dataset['date'] = dataset['date'].map(datetime.datetime.toordinal)

#dataset['category'] = pd.to_numeric(pd.to_numeric())
#dataset.category = dataset.category.apply(pd.to_numeric, errors='coerce')


dataset.drop(['name','product'],axis = 1, inplace = True)

y = dataset.price

dataset['category'] = dataset['category'].astype('category')
dataset['category'] = dataset['category'].cat.codes
print(dataset['category'])

x = dataset.drop(['price'], axis = 1)
print(dataset.head())

count_linear_model(x,y)

#make predictions of the amount of spendings based on a date
y = unique_dates
x = month_price

#model = count_linear_model(x,y)

while True:
    year, month, day = 2020, 1, 1
    today = date.today()
    input_date = datetime.date(year, month, day)
    while today >= input_date:
        print('Put date of the purchase:')
        year = input('Year: ')
        month = input('Month: ')
        day = input('Day: ')
        input_date = datetime.datetime(year, month, day)
        string_date = day+'-'+month+'-'+year
        #predictions = model.predict(string_date)