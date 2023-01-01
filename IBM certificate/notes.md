# MODULE 1: Python Libraries

## 1. Scientifics Computer Libraries:

- Pandas (Data structures and tools)
- NumPy(Arrays & matrices)
- SciPy(Integrals, solving differential equations, optimization)

## 2. Visualization Libraries:
- Matplotlib(plots & graphs,most popular)
- Seaborn(plots: heat maps, time series, violin plots)

## 3. Algorithmic Libraries:

- Scikit-learn(machine learning: regression, classification)
- Statsmodels(explore data, estimate statistical models and perform statistical tests)

# Importing Data

1. Format: various formats: .csv, .json, .xlsx, .hdf
2. File path of dataset
- Computer
- Internet 

# Reading file in pandas

## 1. Import in pandas 

```py
Import pandas as pd
url = “”
```

## 2. Read_csv assumes the data contains a header. Using df to not assign headers by setting header to none

```py
df = pd.read_csv(url, header = None)
```
- df prints the entire dataframe
- df.head(n) prints the first n row of dataframe
- df.tail(n) prints the last n row of dataframe
- df.info() prints information about the dataframe: number of columns, column labels, column data types, memory usage, range index, and the number of cells in each column (non-null values)

## 3. Adding headers
Replace default header by

```py
headers = []
df.columns = headers
```
## 4. Export to CSV

```py
path=""
df.to_csv(path)
```

# Analyse data in pandas

## 1. Check data types

Use df.dtyes to check data types

## 2. Return statical summary 

Use df.describe()

# Accessing databases using Python

DB-API is Python's standard API for accessing relational databases.

## Methods used with connection objects

- cursor() returns a new cursor object using the connection
- commit() uses to commit any pending transaction to the database
- rollback() causes the database to rollback to the start of any pending transactions
- close () is used to close a database connection

## Write code using DB-API

```py
from dbmodule import connect 

#Create connection object
connection = connect('databasename','username','pswd')

#Create a cursor object
cursor = connection.cursor()

#Run queries
cursor.execute('select * from table')
results = cursor.fetchall()

#Free resources
Cursor.close()
connection.close()
```

# MODULE 2: Data Pre-processing (Data Cleaning or Data Wrangling)

## Access a column by specifying the name of the column

Eg: df["symboling"]

## Manupulate dataframe in python

Eg: to add one to each symboling entry use df 

```py
["symboling"] =df["symboling"]+1

```

## Dealing with missing values in Python

Missing values occurs when no data value is stored for a variable in an observation.
Example of missing data could be "?", "N/A" or 0 or just a blank cell.

1. Check with the data collection source
2. Drop the missing values
    - Drop the variable
    - Drop the data entry

3. Replace the missing values
    - replace it with an average
    - replace it by frequency
    - replace it based on other functions

4. Leave it as missing data 

### Drop missing values in Python

    - Use dataframes.dropna()
 ```py
 df.dropna(subset=["price"]), axis=0, inpace = True
 #axis=0 drops the entire row
 #axis=1 drops the entire column
 ```

![Alt text](https://file%2B.vscode-resource.vscode-cdn.net/Users/buithuytien/Desktop/Screen%20Shot%202022-11-28%20at%205.36.57%20pm.png?version%3D1669617616779)

Link for further information: http://pandas.pydat.org/

### Replace missing values in Python:

    - Use dataframe.replace(missing_value, new value)
    - To find mean use dataframe.mean()

## Data Formatting

- Formatted data: more clear, easy to aggregate and easy to compare
- Incorrect data types:
    Use dataframe.dtypes() to identify data type
    Use dataframe.astype() to convert data type

## Data normalization

- Simple Feature scaling

xnew = xold/xmax

Eg

```py
df["length"] = df["length"]/df["length"].max()
```

- Min-Max

xnew = xold-xmin/xmax-xmin

Eg:

```py

df["length"] = (df["length"]-df["length"].min())/
                (df["length"].max-df["length"].min())

```

- Z-score

x new = subtract the mu which is the averge of the feature and then divide by the standard deviation sigma.

```py

df["length"] = (df["length"]-df["length"].mean())/df["length"].std()

```

## Binning in Python

- Binning: grouping of values into "bins"
- Coverts numeric into categorial variables
- Group a set of numerical values into a set of "bins"

## Turn categorial variables into quantitative variales in Python

- Use pandas.get_dummies() method to convert categorial variables to dummy variables (0 or 1)

# Exploratory Data Analyst (EDA)

Purpose:

- Summarise main characteristics of data
- Gain better understanding of the data set 
- Uncover relationships between variables
- Extract important variables

## Descriptive statistics

- Describe basic features of the data
- Giving short summarises about the sample and measures of the data

## Describe()

- Summarise statistics using pandas describe()

```py
df.describe()

```
## Value_count()
- Summarise the categorical data by using the Value_count() method

## Box plot

- Box plot make it easier to compare between group 

![Alt text](https://file%2B.vscode-resource.vscode-cdn.net/Users/buithuytien/Desktop/Screen%20Shot%202022-12-03%20at%2010.24.52%20pm.png?version%3D1670066714739)

## Scatter plot

- Each observation represented as a point

- Scatter plot show the relationship between two variables
1. Predictor/independent variables on x-axis
2. Target/dependent variables on y-axis

## Group by 

```py
df.groupby()
```
## Model
- A model can be thought as a  mathematical equation used to predict a value given one or more other values
- Relating one or more independent variables to dependent variables
- Usually the more relevant data you have the more accurate your model is 
- Different types of models:
1. Simple linear regression
2. Multiple linear regression
3. Polynomial regression

### Simple and multiple linear regression

- Linear regression will refer to one independent variable to make a prediction
- Multiple linear regression will refer to multiple independent varibales to make a prediction
- Simple Linear regression (SLR) helps to understand the relationship between two variables
1. The predictor (independent) variable x
2. The target (dependent) variable y
- Fit a model in Python
1. Import linear_model from scikit-learn
```py
from sklearn.linear_model import LinearRegression
```
2. Creat a linear regression obkect using the construction:
```py
lm = LinearRegression()
```
3. Define the predictor variable and target variable
```py
X = df[['highway-mpg']]
Y = df['price']
```
4. Then use lm,fit(X,Y) to fit the model
```py
lm.fit(X, Y)
```
5. Obtain prediction using method predict
```py
Yhat=lm.predict(X)
```
- Multiple linear regression is used to explain the relationship between:
1. One continuous target (Y) variable
2. Two or more predictor (X) variables
- Fit a multiple linear model estimator
1. Extract 4 predictor variables and store them in variable Z
```py
Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
```
2. The train the model
```py
lm.fit(Z, df['price'])
```
3. Obtain a prediction
```py
Yhat=lm.predict(X)
```
- Regression Plot
1. The relationship between two variables
2. The strengh of the correlation
3. The direction of the relationship (positive or negative)

- Polynomial Regression
1. A special case of the general linear regression model
2. Useful for describing curvilinear relationships

- Pipelines
There are many steps to getting a prediction
normalisation --> polynomial transform --> linear regression

- Two important measures to determine the fit of a model:
1. Mean Squared Error (MSE)
2. R-squared (R^2): the coefficient of determination. It is measure to determine how close the data is to the fitted regression line. 

## Model Evaluation
- Seperating data into training and testing sets is an important part of model evaluation
- Usually large portaion of data is used for training and a smaller part is used for testing
- train_test_split(): split data into random train and test subsets

## Generalization performance: 

- Generalization error is measure of how well our data does at predicting previously unseen data

## Ridge Regression
- Ridge regression is a regression that is employed in a multiple regression model when multicollinearity occurs
- Multicollinearity is when there is a strong relationship among the independent variables
- to make a predicion using rigde regression
- the model that exhibits overfitting is usually the model with the lowest parameter value for alpha

```py
from sklearn.linear_model import Ridge
RidgeModel=Ridge(alpha=0.1)
 RidgeModel.fit(X,y)
 Yhat=RidgeModel.predict(X)
```

## Grid search 

- allows us to scan through multiple free parameters with few lines of code

























