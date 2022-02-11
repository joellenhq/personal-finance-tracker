import seaborn as sns
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
#from sklearn import *

def count_linear_model(x,y):
    #random train test split causes problem
    #x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=0)
    if len(x)>20:
        split = int(x.shape[0] * .9)

        x_train = x[:split]
        y_train = y[:split]
        x_test = x[split:]
        y_test = y[split:]
    else:
        x_train = x
        y_train = y

    lr = linear_model.LinearRegression()
    lr.fit(x_train, y_train)
    if len(x) > 20:
        acc = lr.score(x_test, y_test)
        #print(acc)
    #print('Coefficient: \n', lr.coef_)
    #print("Intercept: \n", lr.intercept_)
    return lr

dataset = pd.read_csv('cosmetics-spendings.csv',encoding='cp1252')
print(dataset.head())
#print(dataset.tail())

print(dataset.describe().T)
#print(dataset['category'].unique())
#print(dataset.shape)

categories = ['gift','face care','additional care','everyday care','make-up']

plt.figure(figsize=(10,6))
plt.title('Product prices')
sns.scatterplot(data=dataset, x='date', y='price')  #,hue='category')
plt.xlabel('Date of purchase')
plt.ylabel('Price of product [zł]')

#plt.show()

#print(dataset['date'].unique())
unique_dates = ['30.11.2020','05.01.2021','21.01.2021','18.02.2021','11.06.2021',
'06.07.2021','19.08.2021','20.09.2021','19.11.2021','07.01.2021']

month_price=np.zeros(len(unique_dates))
for i,data in enumerate(unique_dates):
    particular_date = dataset.loc[dataset.date == data]
    for value in particular_date.price:
        month_price[i] = month_price[i] + value
#print(month_price)

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
#dataset['date'] = pd.to_datetime(dataset['date'])
#dataset['date'] = dataset['date'].map(datetime.datetime.toordinal)

for i, data in enumerate(dataset.date):
    particular_date = dataset.loc[i, 'date']

    day,month,year = particular_date.split('.')
    dataset.loc[i, 'date'] = int(month) + int(day)

#print(dataset['date'])

#dataset['category'] = pd.to_numeric(pd.to_numeric())
#dataset.category = dataset.category.apply(pd.to_numeric, errors='coerce')


dataset.drop(['name','product'],axis = 1, inplace = True)

y = dataset.price

dataset['category'] = dataset['category'].astype('category')
dataset['category'] = dataset['category'].cat.codes

x = dataset.drop(['price'], axis = 1)
#print(dataset.head())

count_linear_model(x,y)

months = np.ones(len(unique_dates))
days = np.ones(len(unique_dates))
for i,data in enumerate(unique_dates):
    day,month,year = data.split('.',3)
    months[i] = int(month)
    days[i] = int(day)


#make predictions of the amount of spendings based on a date
x1 = pd.Series(months)
x2 = pd.Series(days)

d = {'col1': x1, 'col2': x2 }
x = pd.DataFrame(d)
y = pd.Series(month_price).values.reshape(-1, 1)
#print(y)
#print(y.shape)
#print(x.shape)
#print(x)

model = count_linear_model(x,y)

print('Put date of the purchase:')
year1 = input('Year: ')
month1 = int(input('Month: '))
day1 = int(input('Day: '))
string_date = str(day1)+'-'+str(month1)+'-'+str(year1)
x1 = pd.Series(month1)
x2 = pd.Series(day1)
d = {'col1': x1, 'col2': x2}
input = pd.DataFrame(d)

#print(input)
#print(input.shape)
input = np.array(input)#.reshape(-1,1)

predictions = model.predict(input)
predictions = round(predictions[0,0],2)
print('You will probably spend: ',predictions,' zł')