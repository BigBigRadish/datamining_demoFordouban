#coding=utf-8
#̽探索变量之间的关系
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn import  datasets,linear_model
from pandas import  Series,DataFrame
from numpy import random 
from scipy import  stats
tips=pd.read_csv('E:\webJRE\PyDemo1\\tips.csv');#导入文件
tips['tip_pct']=tips['tip']/tips['total_bill']
#可视化变量之间的关系
sns.set()
sns.pairplot(tips, hue="day",kind='reg')#散点图
plt.show(sns)
#一个线性关系的训练模型
#load the diabetes dataset
diabetes =datasets.load_diabetes()
#use only the Feature
diabeats_X=diabetes.data[:,np.newaxis,2]
#split the data into training/testing sets
diabeats_X_train=diabeats_X[:20]
diabeats_X_test=diabeats_X[-20:]
#split the targets into training/testing sets
diabeats_Y_train=diabeats_X[:20]
diabeats_Y_test=diabeats_X[-20:]
#CREAT linear regression object
regr=linear_model.LinearRegression()
#  using the train sets train the model
regr.fit(diabeats_X_train, diabeats_Y_train)
#the coefficients
print('Coefficient: \n',regr.coef_)
#the mean squre ERROR
print("Residual sum of squares: %.2f" 
      % np.mean(regr.predict(diabeats_X_test)-diabeats_Y_test)**2)
# explored variance score:1 is more perfect prediction
print ("variance score: %.2f"
       % regr.score(diabeats_X_test,diabeats_Y_test))
# plot outputs
plt.scatter(diabeats_X_test,diabeats_Y_test,color='black')
plt.plot(diabeats_X_test,regr.predict(diabeats_X_test),color='blue',linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()