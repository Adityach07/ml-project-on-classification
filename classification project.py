# -*- coding: utf-8 -*-
"""project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FPIybW5Xg7eKGTDs8FNHMJ5zYAKCqwr0

**Project Name:** Diabetes prediction

**Problem** **Statement:**

Build a machine learning model that predicts whether the person is effected by diabetes or not.

**Data Collection , Data preprocessing**
"""

import pandas as pd
import numpy as np

df=pd.read_csv('/content/diabetes.csv')
df.head()

"""**Data preproccesing**"""

df.isnull().sum()

df.info()

df.shape

df.describe()

df.duplicated().sum()

df.isnull()

df_new=df
df_new[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']]=df[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0, np.NaN)

df_new["Glucose"].fillna(df_new["Glucose"].mean(), inplace = True)
df_new["BloodPressure"].fillna(df_new["BloodPressure"].mean(), inplace = True)
df_new["SkinThickness"].fillna(df_new["SkinThickness"].mean(), inplace = True)
df_new["Insulin"].fillna(df_new["Insulin"].mean(), inplace = True)
df_new["BMI"].fillna(df_new["BMI"].mean(), inplace = True)

df_new.isnull().sum()

df['Outcome'].value_counts()

"""Data visulization"""

import matplotlib.pyplot as plt
import seaborn as sns

df.hist(figsize=(30,30))

corelation=df.corr()

sns.heatmap(corelation,annot=True)
plt.show()

"""Feature selection"""

df1 = df.copy()

age_bins = [0, 18, 35, 50, 65, 100]
age_labels = ['0-18', '19-35', '36-50', '51-65', '66+']

df1['Age_Group'] = pd.cut(df1['Age'], bins=age_bins, labels=age_labels, right=False)
df1

bmi_bins = [0, 18.5, 24.9, 29.9, float('inf')]
bmi_labels = ['Underweight', 'Normal', 'Overweight', 'Obese']

df1['BMI_Category'] = pd.cut(df1['BMI'], bins=bmi_bins, labels=bmi_labels, right=False)
df1

df1['Insulin_Glucose_Ratio'] = df1['Insulin'] / df1['Glucose']
df1

"""**Model Training**"""

from sklearn.model_selection import train_test_split

x= df.drop('Outcome', axis=1)
y= df['Outcome']

x

x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42,test_size=0.2)

x_train

y_train

"""***Model selction***"""

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

model_lr=LogisticRegression()
model_lr.fit(x_train, y_train)
y_pred_lr = model_lr.predict(x_test)

y_pred_lr

"""**Model Evaluation:**

"""

from sklearn.metrics import accuracy_score, precision_recall_fscore_support, classification_report,confusion_matrix

y_pred_lraccuracy_lr = accuracy_score(y_test, y_pred_lr)
precision_lr, recall_lr, f1_lr, _ = precision_recall_fscore_support(y_test, y_pred, average='weighted')
print(classification_report(y_test, y_pred_lr))
print("Accuracy:", accuracy_lr)
print("Precision:", precision_lr)
print("Recall:", recall_lr)
print("F1 Score:", f1_lr)

matrix=confusion_matrix(y_test,y_pred_lr)
sns.heatmap(matrix, annot=True)
plt.show()

"""**Model 2**"""

from sklearn.tree import DecisionTreeClassifier
model_dr=DecisionTreeClassifier()
model_dr.fit(x_train, y_train)
y_pred_dr = model_dr.predict(x_test)

y_pred_dr

accuracy_dr = accuracy_score(y_test, y_pred_dr)
precision_lr, recall_lr, f1_lr, _ = precision_recall_fscore_support(y_test, y_pred_dr, average='weighted')
print(classification_report(y_test, y_pred_lr))
print("Accuracy:", accuracy_dr)
print("Precision:", precision_lr)
print("Recall:", recall_lr)
print("F1 Score:", f1_lr)

matrix=confusion_matrix(y_test,y_pred_dr)
sns.heatmap(matrix, annot=True)
plt.show()

"""**Model 3**"""

from sklearn.svm import SVC
model_svc=SVC()
model_svc.fit(x_train, y_train)
y_pred_svc = model_dr.predict(x_test)

y_pred_svc

accuracy_svc = accuracy_score(y_test, y_pred_svc)
precision_svc, recall_svc, f1_svc, _ = precision_recall_fscore_support(y_test, y_pred_svc, average='weighted')
print(classification_report(y_test, y_pred_svc))
print("Accuracy:", accuracy_svc)
print("Precision:", precision_svc)
print("Recall:", recall_svc)
print("F1 Score:", f1_svc)

matrix=confusion_matrix(y_test,y_pred_svc)
sns.heatmap(matrix, annot=True)
plt.show()

"""**Saving The Model**"""

import pickle

with open ('lr_pickle','wb') as file:
  pickle.dump(model,file)

with open('/content/lr_pickle','rb') as file:
  LR=pickle.load(file)

LR.coef_
