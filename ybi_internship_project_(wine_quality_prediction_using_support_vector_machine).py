# -*- coding: utf-8 -*-
"""YBI internship project (Wine quality prediction using support vector machine).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XMzDVUkNcOoVjmDI4wKEty0blIlIRCUt

Import Libraries
"""

import pandas as pd

import numpy as np

"""Import CSV as DataFrame"""

df = pd.read_csv('https://github.com/YBIFoundation/Dataset/raw/main/WhiteWineQuality.csv', sep=';')

df.head()

df.info()

df.describe()

df.columns

df.shape

df['quality'].value_counts()

df.groupby('quality').mean()

"""Define target variable (y) and independent variable (X)"""

y = df['quality']

y.shape

y

X = df[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol']]

X.shape

X

"""Get X variables standardized"""

from sklearn.preprocessing import StandardScaler

ss = StandardScaler()

X = ss.fit_transform(X)

X

"""Get Train Test Split"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state = 2529)

X_train.shape, X_test.shape, y_train.shape, y_test.shape

"""Get Model Train"""

from sklearn.svm import SVC

svc = SVC()

svc.fit(X_train, y_train)

"""Get Model Prediction"""

y_pred = svc.predict(X_test)

y_pred.shape

y_pred

"""Get Model Evaluation"""

from sklearn.metrics import confusion_matrix, classification_report

print(confusion_matrix(y_test, y_pred))

print(classification_report(y_test, y_pred))

"""Get model re-run with two classes created for wine quality

Wine quality 3,4,5 labelled as 0
Wine quality 6,7,8,9 labelled as 1
"""

y = df['quality'].apply(lambda y_value: 1 if y_value>=6 else 0)

y.value_counts()

"""Get train test split"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state = 2529)

X_train.shape, X_test.shape, y_train.shape, y_test.shape

"""Get Model Train"""

from sklearn.svm import SVC

svc = SVC()

svc.fit(X_train, y_train)

"""Get Model Prediction"""

y_pred = svc.predict(X_test)

y_pred.shape

y_pred

"""Get Model Evaluation"""

from sklearn.metrics import confusion_matrix, classification_report

print(confusion_matrix(y_test, y_pred))

print(classification_report(y_test, y_pred))

"""Get Future Predictions

Steps:
1. Extract a random row using sample function
2. Separate X and y
3. Standardize X
4. Predict
"""

df_new = df.sample(1)

df_new

df_new.shape

X_new = df_new.drop(['quality'], axis=1)

X_new = ss.fit_transform(X_new)

y_pred_new = svc.predict(X_new)

y_pred_new