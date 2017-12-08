#coding=utf-8
#̽探索变量之间的关系
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import  Series,DataFrame
from numpy import random 
from scipy import  stats
tips=pd.read_csv('E:\webJRE\PyDemo1\\tips.csv');#导入文件
print tips;
print tips.dtypes;
#fig=plt.figure(figsize=(8,6)) #用于绘图的大框
#ax=fig.add_subplot(1,3,1)#生成一个小框最后那个参数表示被分割的第几个
#ax.plot(random.rand(50).cumsum(),'o')#生成50个均匀分布的随机数
#plt.show(fig);
fig,ax=plt.subplots(1,1,figsize=(6,6))#分割成几行几列，然后是总的画布大小，默认第一个
#画出离散图，画出性别离散图
#ax.plot(tips[tips['sex']=='Male']['tip'],'o',label='Male')
#ax.plot(tips[tips['sex']=='Female']['tip'],'o',label='Female') 
#ax.legend(loc='best')
#plt.show(fig);
#ax.plot(tips[tips['sex']=='Male']['total_bill'],tips[tips['sex']==' Male']['tip'],'o',label='Male')
#ax.plot(tips[tips['sex']=='Female']['total_bill'],tips[tips['sex'] =='Female']['tip'],'o',label='Female')
#ax.legend(loc='best')
#plt.show(fig);
#独立性检验
count=pd.crosstab(tips.sex, tips.day) 
count.T.plot(kind='bar') 
chi2, p, dof, ex = stats.chi2_contingency(count, correction=False);#进行卡方检验，chi2代表卡方统计量，p代表p值，dof代表自由度，ex代表频率