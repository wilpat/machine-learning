#Simple Linear Regression
dataset = read.csv('Salary_Data.csv')

#Splitting the dataset into training and test set (We need "caTools")
library(caTools)
set.seed(123) #The replica of random_state in python
split = sample.split(dataset$Salary, SplitRatio = 2/3)#Perform the split-- It doesnt matter what column you choose
training_set = subset(dataset, split == TRUE) #Apply the split on the dataset to generate the training
test_set = subset(dataset, split == FALSE)

#Feature scaling -- We need to exclude the columns with encoded categorical data (If any)
#This exclusion is done by specifying the unencoded data columns to be scaled
#training_set[, 2:3] = scale(training_set[, 2:3])
#test_set[, 2:3] = scale(test_set[, 2:3])

#We didnt need to scale because linear regression class takes care of that for us out of the box

#Fitting the linear regression to the training set -- Generate the model the program should use
regressor = lm(formula = Salary ~ YearsExperience,
               data = training_set)
#Above, you want to specify what columns are proportional in the dataset that you provide

#To properly view the details of the regressor, use the console to execute "summary(regressor)"

#Predicting the test set results 
y_pred = predict(regressor, newdata = test_set)

#Visualizing the training_set results
# install.packages('ggplot2')
library(ggplot2)
ggplot() +
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             colour = 'red') + #Plot the scatter points of the training observations
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            colour = 'blue') + #Draw a regression line based on the model applied on the training set
  ggtitle('Salary vs Experience (Training Set)') +
  xlab('Years Of Experience') +
  ylab('Salary')

#Visualizing the test_set results
ggplot() +
  geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary),
             colour = 'red') +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            colour = 'blue') + #Like in python, we dont need to use d test data to plot a new reg line as they would give line of same slope
  ggtitle('Salary vs Experience (Test Set)') +
  xlab('Years Of Experience') +
  ylab('Salary')
  