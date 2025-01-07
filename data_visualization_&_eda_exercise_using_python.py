# -*- coding: utf-8 -*-
"""Data_Visualization & EDA Exercise Using Python.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1k0fPtDlq45PpLWYJHBSuwdrLb6SpmGNl
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as snr

iris=snr.load_dataset('iris')

"""![Description-of-IRIS-dataset-showing-Petal-length-Sepal-length-Petal-width-and-Sepal.png](data:image/png;base64,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)"""

iris.head()

iris.tail()

#Line Graph
ax=iris.plot(figsize=(10,5),title='Iris Dataset')
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")

#Line Graph
ax=iris['sepal_width'].plot(figsize=(10,5),title='Iris Dataset')
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")

ax=iris['petal_length'].plot(figsize=(10,5),title='Iris Dataset')
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")

ax=iris['petal_width'].plot(figsize=(10,5),title='Iris Dataset')
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")

ax=iris['sepal_length'].plot(figsize=(10,5),title='Iris Dataset')
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")

df=iris.drop(['species'],axis=1)

df.head()

df.plot(kind='bar')

df.iloc[0].plot(kind='bar')

df.iloc[0].plot(kind='barh')

df.iloc[50].plot(kind='bar')

df.iloc[50].plot(kind='barh')

df.iloc[100].plot(kind='bar')

df.iloc[0:4].plot(kind='bar')

df.iloc[100:104].plot(kind='bar')

df.plot(kind='hist',bins=200) #thickness of the histogram

df['sepal_length'].diff().plot(kind='hist',bins=200)

df['sepal_width'].diff().plot(kind='hist',bins=200)

df['petal_length'].diff().plot(kind='hist',bins=200)

df.iloc[0].plot.pie(figsize=(5,5),fontsize=10,autopct='%.2f')

df.iloc[100].plot.pie(figsize=(5,5),fontsize=10,autopct='%.4f')

df.iloc[50].plot.pie(figsize=(5,5),fontsize=10,autopct='%.4f')

df.iloc[0:3].plot.pie(subplots=True,figsize=(12,12),fontsize=10,autopct='%.2f')

df.iloc[0:5].plot.pie(subplots=True,figsize=(12,12),fontsize=10,autopct='%.2f')

"""Advanced Visualizations - Exploratory Data Analysis (EDA)

1. Scatter Plot

2. Relational Plot

3. Box Plot

4. Pair Plot

5. Heatmap (basics of ML)

6. Cat Plot
"""

data=pd.read_csv("/content/tips.csv")

data.head()

data.plot.scatter(x='total_bill',y='tip',color='g')

snr.relplot(x='total_bill',y='tip',data=data)

snr.relplot(x='total_bill',y='tip',hue='sex',style='smoker',data=data) #style is a parameter which gives shapes to the categories - any coloum we put inside style, the categories inside will get a shape

snr.relplot(x='total_bill',y='tip',hue='sex',style='smoker',col='day',data=data) #col is a parameter which will give number of plots same as number of categories in the column

snr.relplot(x='total_bill',y='tip',hue='sex',style='smoker',size='size',data=data)

"""Q. Visualize the relation between total bill collected and tip for lunch and dinner time using relational plot"""

snr.relplot(x='total_bill',y='tip',col='time',data=data)

snr.pairplot(data)

snr.catplot(x='day',y='total_bill',hue='sex',data=data)

snr.catplot(x='day',y='total_bill',hue='sex',kind='bar',data=data)

snr.catplot(x='day',y='total_bill',hue='sex',kind='strip',data=data)

snr.catplot(x='day',y='total_bill',hue='sex',kind='violin',data=data)

snr.catplot(x='day',y='total_bill',hue='sex',kind='box',data=data)

