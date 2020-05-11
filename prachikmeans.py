# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 20:32:26 2019

@author: SANIYA
"""
#importing libraries
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd

n=int(input("enter the no of clusters: "))

#loading data 
df=pd.read_csv("C:\\Users\\SANIYA\\Desktop\\fact.csv")
data=[]
for i in range(len(df)):
    data.append([df.iloc[i,0],df.iloc[i,1]])

#kmeans algorithm
kmeans = KMeans(n_clusters=n).fit(data)
print(kmeans.labels_)
centroids = kmeans.cluster_centers_
print(centroids)

#splitting data
sales=[]
profit=[]
for x in range(len(data)):
    sales.append(data[x][0])
    profit.append(data[x][1])
    
#plotting clusters and their centroids
plt.scatter(sales, profit, s = 30)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=100)


