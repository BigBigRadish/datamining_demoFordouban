#coding=utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import  Series,DataFrame
tips=pd.read_csv('E:\webJRE\PyDemo1\\tips.csv');#
df1=DataFrame(np.random.randn(10,4),columns=['a','b','c','d'],index=np.arange(0,100,10));#随机生成10*4的正态分布随机数，属性名分别为a，b，c，d，index的值为(0,100)10个数
print df1;
plt.show (df1.plot());#python中图片的输出方式、
plt.show (df1.plot(style='o----'));#python中图片的输出方式,每个数值为一个节点，用虚线进行连接，o表示远点
plt.show (df1.plot(kind='bar'));#柱形图正向
plt.show (df1.plot(kind='barh'));#柱形图转向
#列联表
count=pd.crosstab(tips.sex,tips.day)#通过列联表，可以查看一周每一天对应的男性和女性，列轴是第一个参数，要统计的，横轴是name
print count
plt.show(count.plot(kind='bar'));#方便显示不同属性的具体天数
plt.show(count.T.plot(kind='bar'))#关于每天的男性与女性人数的比较
count1=pd.crosstab(tips.sex,tips.smoker)
plt.show(count1.T.plot(kind='bar'));
tips['tip_pct']=tips['tip']/tips['total_bill']#每天小费所占的百分比
print tips;
plt.show(tips['tip_pct'].hist(bins=50))#划分50个区间，看有多少横坐标落到当前区间
#例子：一只股票每日收益率为0.1%，每日波动率为0.5%，求100日后的预期收益率？
#由题设可知，这只股票服从u=0.1，σ=0.5的正态分布
changes=DataFrame(np.random.normal(loc=0.1,scale=0.25,size=(100,100)))
print changes
returns =changes.cumsum(0)
print returns;
plt.show(returns.plot())