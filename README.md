# Used Car Price Prediction


## Table of Content
  * [Demo](#demo)
  * [Problem Statement](#problem-statement)
  * [Approach](#approach)
  * [Technologies Used](#technologies-used)
  * [Installation](#installation)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Bugs & Logs](#bugs--logs)
  * [Contributors](#contributors)

## Demo
Link: [https://car-price-prediction-new1.herokuapp.com/](https://car-price-prediction-new1.herokuapp.com/)

![car](https://user-images.githubusercontent.com/76767335/171604645-fdc189e3-0206-4f68-99f2-bca18a3b0f7b.gif)


## Problem Statement
The prices of new cars in the industry is fixed by the manufacturer with some additional costs incurred by the Government in the form of taxes. So, customers buying a new car can be assured of the money they invest to be worthy. But due to the increased price of new cars and the incapability of customers to buy new cars due to the lack of funds, used cars sales are on a global increase (Pal, Arora and Palakurthy, 2018). There is a need for a used car price prediction system to effectively determine the worthiness of the car using a variety of features. 

Even though there are websites that offers this service, their prediction method may not be the best. Besides, different models and systems may contribute on predicting power for a used car’s actual market value. It is important to know their actual market value while both buying and selling.

## Approach
Data Exploration : Exploring dataset using pandas, numpy.

Feature Engineering : Removed missing values and created new features as per insights.

Model Building & Testing : Tried many machine learning algorithms and checked the base accuracy to find the best fit.

Pickle File : Created pickle file as per need.

Building web app : Building web app using python and Flask.

User Interface & deployment :  Created an UI that shows the output.
                          After that I have deployed project on heroku.
## Technologies Used
 
   1. Python 
   2. Pandas
   3. Numpy
   4. Sklearn
   5. matplotlib
   6. seaborn
   7. Flask

## Dataset
[Download here](https://github.com/Shankar297/Used-Car-Price-Prediction/blob/master/car_dataset.csv)

## Installation
Click here to install [python](https://www.python.org/downloads/). To install the required packages and libraries, run this pip command in the project directory after cloning the repository:
```bash
git clone https://github.com/Shankar297/Used-Car-Price-Prediction.git
```

```bash
pip install -r requirements.txt
```
If pip is not already installed, Follow this [link](https://pip.pypa.io/en/stable/installation/)

## Deployement on Heroku
Create a virtual app on Heroku website. You can either connect your github profile or download cli to manually deploy this project.
Follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

## Bugs & Logs

1. If you find a bug, kindly open an issue and it will be addressed as early as possible.
2. Under localhost, logging is performed for all the actions and its stored onto logs.txt file
3. When the app is deployed on heroku, logs can be viewed on  heroku dashboard or CLI.

## Contributors
  [Shankar Wagh](https://github.com/Shankar297)
