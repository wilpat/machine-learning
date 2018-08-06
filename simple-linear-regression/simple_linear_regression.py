# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 01:13:22 2018

@author: William
"""

#Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values #Matrix of features i.e independent vars
y = dataset.iloc[:, 1].values


#Splitting dataset into training and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

#Feature Scaling -- Used to make all the content of the dataset be of the same scale
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

#Fitting the Simple Linear Regression to the training set
#This basically means making the program learn the correlation between the
#Independent and dependent variable.
#This is also how you make the model for the program
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#Predict Test Set Result
y_pred = regressor.predict(X_test)

#Visualizing the results 
#The independent variable would be on the y-axis and vice-versa

#First plot the observation points of the real values
plt.scatter(X_train, y_train, color='red')
#Plot the regression line i.e the predictions
plt.plot(X_train, regressor.predict(X_train), color ='blue')
plt.title('Salary vs Experience (Training Set)')
plt.xlabel('Years Of Experience')
plt.ylabel('Salary')
plt.show()

#Now plot the observation points of the test values
plt.scatter(X_test, y_test, color='red')
#Below, it doesnt matter if u use x_test or train, the line remains the same
#The length could differ but the slope is the same
plt.plot(X_train, regressor.predict(X_train), color ='blue')
plt.title('Salary vs Experience (Test Set)')
plt.xlabel('Years Of Experience')
plt.ylabel('Salary')
plt.show()
