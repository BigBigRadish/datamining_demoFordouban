#coding=utf-8
#分类和预测
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn import  datasets,linear_model,datasets
from pandas import  Series,DataFrame
from numpy import random 
from scipy import  stats
from sklearn.linear_model.base import LinearRegression
#线性回归
#clf=linear_model.LinearRegression();
#clf.fit(X, y)
#clf.predict(newx);
#关于花的分类
#import iris data
iris =datasets.load_iris()
x=iris.data[:, :2]
y= iris.target;
h=.02#step size in the mesh
#logreg =linear_model.LogisticRegression(c=1e5)
tips=pd.read_csv('E:\webJRE\PyDemo1\\tips.csv');#导入文件
tips['tip_pct']=tips['tip']/tips['total_bill']
x=np.array([tips['tip'],tips['size']]).T
y=np.array([tips['total_bill']]).T
clf=linear_model.LinearRegression();#线性回归
clf.fit(x,y)
LinearRegression(copy_X=True,fit_intercept=True,n_jobs=1,normalize=False)
print clf.intercept_;
print clf.coef_;