#Regression Template
dataset = read.csv('Position_Salaries.csv')

#Specifying a specific part of your dataset you want to work with


# Fitting Regression Model to the dataset

install.packages('randomForest')
library(randomForest)
set.seed(1234)

regressor = randomForest(x = dataset[1],
                         y = dataset$Salary,
                         ntree = 500)

#Predicting the salary with the regression model
y_pred = predict(regressor, data.frame(Level = 6.5))


#Visualize with smoother curve
library(ggplot2)

x_grid = seq(min(dataset$Level), max(dataset$Level), 0.01)

ggplot()+
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             colour = 'red')+ #Plot the scatter points of the training observations
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Level = x_grid))),
            colour = 'blue')+ #Draw a regression line based on the model appliedset
  ggtitle('Truth or Bluff(Regression Model)')+
  xlab('Organizational Level')+
  ylab('Salary')



