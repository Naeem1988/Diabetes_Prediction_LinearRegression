# -*- coding: utf-8 -*-
"""LinearRegression_Diabetes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MYxJeTxeveER1n4bZdH4m1f1TKcGKw-P
"""

import matplotlib.pylab as plt
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn import datasets

diabetes = datasets.load_diabetes() # load data
diabetes.data.shape # feature matrix shape

diabetes.target.shape # target vector shape

diabetes.feature_names # column names

# Sperate train and test data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target, test_size=0.2, random_state=12)

model = LinearRegression()
model.fit(X_train, y_train)
model.coef_ # Get the coefficients, beta

model.intercept_ # Get the intercept, c

"""**R-squared** is the proportion of variance explained. It is the proportion of variance in the observed data that is explained by the model.
**R-squared is between 0 and 1** : Higher values are better because it means that more variance is explained by the model.
The threshold for a good R-squared value depends widely on the domain. Therefore, it's most useful as **a tool for comparing different models**
"""

model.score(X_test, y_test)

y_Pred=model.predict(X_test)

"""Visualizing the actual y and the predicted y values...."""

import pandas as pd

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_Pred})
df1 = df.head(25)
df1.plot(kind='bar',figsize=(6,6))
plt.show()

