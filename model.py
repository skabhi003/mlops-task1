# importing pandas module to load the dataset

import pandas as pd 
dataset = pd.read_csv('Salary_Data.csv')
dataset.head()
dataset.columns
dataset.info()
X = dataset['YearsExperience']
y = dataset['Salary']

# importing linear regression function to train our model

from sklearn.linear_model import LinearRegression
model = LinearRegression()
X = X.values.reshape(-1,1)
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model.fit(X_train,y_train)

import joblib 
joblib.dump(model,'salary.pk1')
