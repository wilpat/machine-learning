# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 11:38:17 2018

@author: William
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')

X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values


#Create and fit a Random Forest Regression to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 300, random_state = 0)
#n_estimator depicts the number of trees to be used in this regression
#The more the trees the better your predictions
#Similar to polynomial regression
regressor.fit(X,y)

#Predict a new result
y_pred = regressor.predict(6.5)

#Visualize the Random Forest Regression

#Random forest regression can only be clearly visualized with
#points given a very small interval
#Set the scale at which the x-axis would be plotted
X_grid = np.arange(min(X), max(X), 0.01)
#The above gives an array, so convert to a matrix
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color ='red')
plt.plot(X_grid, regressor.predict(X_grid), color ='blue')
plt.title('Truth or Bluff(Random Forest Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()



