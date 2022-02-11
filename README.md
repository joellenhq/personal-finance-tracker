# personal-finance-tracker
Project was made in order to track cosmetic-product expenses and to predict future spendings with **linear regression model**.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Data visualization](#data-visualization)
* [Money spending prediction](#money-spending-prediction)

## General info
This project is supposed to allow user to track their spendings.
	
## Technologies
Project is created with:
* Python version: 3.9

## Data Visualization

* Plot showing sum of money I spent in hebe shop splitted on particular days. 
![ScreenShot](/screenshots/Overall_spendings.png)

On the basis of that plot it can be indicated that the greatest expences are in particular time of year (close to September).

* Plot with price of every product purchased.
![ScreenShot](/screenshots/Figure_1.png)

Most of the products aren't that expensive so the problem is buying many low-cost products.

* Money spent divided into categories. 
![ScreenShot](/screenshots/Figure_2.png)

The most money I spent on additional care, which is a part that can be restrained in the future.

## Money spending prediction

To predict future expenses **linear regression** machine learning algorithm was used. 
In order to use the dataset it had to be prepared.

Head of data:
|  | date | name | ... | category | price |
| --- | --- | --- | --- | --- | --- |
| 0 | 30.11.2020 |  Bielenda Proffesional Power of Nature | ... |    gift | 35.99 |
| 1 | 30.11.2020 |                     Eveline Cosmetics | ... |    gift | 6.99 |
| 2 | 30.11.2020 |                     Dermika Nasycenie | ... |    gift |  5.99 |
| 3 | 30.11.2020 |                  La Petit Marseillais | ... |    gift |  8.99 |
| 4 | 30.11.2020 |         Allvernum Cedarwood & Vetiver | ... |    gift | 39.99 |

Description of data numeric columns:
[5 rows x 5 columns]
| | count | mean | std | min | 25%  | 50%  |  75%  |  max  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|price  | 67.0 | 11.400448 | 7.988422 | 1.59 | 6.69 | 9.99 | 14.39 | 43.99 |

It was decided that name of the product and its specyfic use would be useless information for the prediction so that the columns name and product were droped.

As the linear regression algorithm accepts only numeric data 'date' and 'category' columns had to be converted into numeric values.
Another issue was that data contained a lot of products with the same date and differrent categories and prices. To make sense of the data it was compressed so that the dataset contained of date and money spent on that day.

Fitted model uses month and day of shopping to predict expenses. User can plan their shopping with this program by inputing the date.

Examples:
![ScreenShot](/screenshots/prediction.png)
