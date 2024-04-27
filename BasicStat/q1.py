"""
a) What type of data is used in this scenario?
-- Numerical data which is also continuous. Continuous data can take any value within a range. In this case, the liters sold and revenue generated can take any value within a range. For example, 100.0, 150.0, 200.0, etc.
b) What is the response variable in this scenario?
-- Revenue generated is the response variable in this scenario. The response variable is the variable that is being predicted or estimated in a statistical model. In this case, the revenue generated is being predicted based on the liters sold.

c) What is the explanatory variable in this scenario?
-- Liters sold is the explanatory variable in this scenario. The explanatory variable is the variable that is used to explain or predict the response variable in a statistical model. In this case, the liters sold is used to predict the revenue generated.

d) What plot is suitable for analyzing the relationship between the variables in this scenario?
-- A scatter plot is suitable for analyzing the relationship between the variables in this scenario. A scatter plot is a graph that shows the relationship between two variables. In this case, the scatter plot will show the relationship between liters sold and revenue generated. The scatter plot will show the relationship between the two variables by displaying the data as a collection of points.

e) How can outliers impact the analysis of the relationship between the variables in this scenario?
-- Outliers can impact the analysis of the relationship between the variables in this scenario. An outlier is a data point that differs significantly from other observations. In this case, an outlier can be a data point that differs significantly from other observations in terms of liters sold and revenue generated. An outlier can impact the analysis of the relationship between the variables in this scenario by skewing the scatter plot and regression line. The scatter plot and regression line can be skewed as the outlier will be plotted as a point on the scatter plot and the regression line will be calculated based on the outlier.

f) What does the slope of the regression line indicate about the relationship between the variables?
-- The slope of the regression line indicates the relationship between the variables. The slope of the regression line indicates the change in the response variable for each unit change in the explanatory variable. In this case, the slope of the regression line indicates the change in revenue generated for each additional liter sold.

g) What insights or conclusions can you draw about the relationship between the variables based on the scatter plot and regression line?
-- The scatter plot and regression line suggest a positive relationship between liters sold and revenue generated. As the liters sold increases, the revenue generated also increases. The slope of the regression line indicates the increase in revenue for each additional liter sold. The scatter plot and regression line also suggest that there are no outliers in the data.



b) What is the relationship between the two variables?
-- The scatter plot and regression line suggest a positive relationship between liters sold and revenue generated. As the liters sold increases, the revenue generated also increases. The slope of the regression line indicates the increase in revenue for each additional liter sold.


"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
data = {
    'Liters': [100.0, 150.0, 200.0, 250.0, 300.0, 350.0, 400.0, 450.0, 500.0, 550.0, 600.0, 700.0, 800.0, 850.0, 900.0, 950.0, 1000.0, 1050.0, 1100.0, 1150.0, 1200.0],
    'Revenue': [200.0, 300.0, 400.0, 500.0, 600.0, 100.0, 800.0, 900.0, 1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1200.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0]
}

df = pd.DataFrame(data)  # creating a dataframe

# Scatter plot
plt.scatter(df['Liters'], df['Revenue'])  # scatter plot
plt.title('Relationship between Liters Sold and Revenue Generated')  # title
plt.xlabel('Liters Sold')  # x label
plt.ylabel('Revenue Generated')  # y label
plt.show()  # displaying the plot

# Linear regression
X = df[['Liters']]  # explanatory variable
y = df['Revenue']  # response variable

model = LinearRegression()  # creating a linear regression model
model.fit(X, y)  # fitting the model

# Plotting regression line
plt.scatter(df['Liters'], df['Revenue'])  # scatter plot
plt.plot(df['Liters'], model.predict(X),
         color='red', linewidth=2)  # regression line
plt.title('Linear Regression: Liters Sold vs Revenue Generated')  # title
plt.xlabel('Liters Sold')  # x label
plt.ylabel('Revenue Generated')  # y label
plt.show()  # displaying the plot

# Slope of the regression line
slope = model.coef_[0]  # slope of the regression line
# displaying the slope of the regression line
print(f'Slope of the regression line: {slope}')

# Conclusion
# The scatter plot and regression line suggest a positive relationship between liters sold and revenue generated.
# The slope of the regression line indicates the increase in revenue for each additional liter sold.
