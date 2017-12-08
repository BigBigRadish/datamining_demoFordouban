#coding=utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import  Series,DataFrame
from scipy import  stats
tips=pd.read_csv('E:\webJRE\PyDemo1\\tips.csv');#导入文件
np.random.seed(5416531)
x=stats.t.rvs(10,size=1000)
print x;
#假设检验
#t统计量
#用数字特征进行检验
print x.max(),x.min(),x.mean(),x.var();#计算理论数字特征
n,(smin,smax),sm,sv,ss,sk=stats.describe(x)#n:大小，sm：均值，sv：svarious，偏差，ss：斜度，sk，峰度
print n,(smin,smax),sm,sv,ss,sk
m,v,s,k=stats.t.stats(10,moments='mvsk')
print m,v,s,k
#更加严格的检验
print 't-statistic=%6.3f pvalue=%6.4f'%stats.ttest_1samp(x,m);#t检验,p值代表置信区间
print stats.kstest(x,'t',(10,))#检验是不是t分布
print stats.kstest(x,'norm',(x.mean(),x.std()))#检验是不是正太分布p值越大，越不能拒绝原假设
#卡方检验
quantities=[0.0,0.01,0.05,0.1,1-0.10,1-0.05,1-0.01,1.0]#假设总体服从正态分布，则他们的平方和服从卡方分布，概率图，列出尾部区间，强调尾部
crit=stats.t.ppf(quantities,10)#数据的分布情况
print crit#输出的分位数
n_sample =x.size;#总体的规模
print np.histogram(x,bins=crit)#按分位数隔断成10个区间
frequent=np.histogram(x,bins=crit)[0];#查看各分位段的样本个数
plt.show(plt.hist(x,bins=crit));#构造直方图
tprob= np.diff(quantities)
print tprob;#算出个区间所占的比例
#用数字特征来判断是不是什么分布,返回什么参数
tdof,tloc,tscale=stats.t.fit(x);#自由度，期望，方差，用fit（）函数进行拟合
print tdof,tloc,tscale
nloc,nscale=stats.norm.fit(x);#用正态分布来拟合数据，返回期望和方差
print nloc,nscale;
#再做卡方检验，检验置信区间
tprob=np.diff(stats.t.cdf(crit,tdof,tloc,tscale));#对t分布做卡方检验
print stats.chisquare(frequent,tprob*n_sample)
nprob=np.diff(stats.norm.cdf(crit,tloc,tscale));#对正态分布做卡方检验
print stats.chisquare(frequent,nprob*n_sample)
#区分正态分布与t分布，应该用尾部进行检验，因为中间的基本上差不多，不好区分
#假设检验，正态分布标准化（标准化公式）之后，比较其值是否落在标准正态分布的边缘区域，如果，，5%，则拒绝原假设
print stats.normaltest(tips['tip'])#查看tip是否是正态分布，p值过小，拒绝原假设
tips['pct']=tips['tip']/tips['total_bill']#百分比
print stats.normaltest(tips['pct'])#查看pic是否是正态分布，p值过小，拒绝原假，形状像正态分布，但是p值过小，可能由异常点引起
print tips[tips['pct']<0.1]#找出异常点
tips1=tips.drop([67,172,178])#去掉尾部异常点
print stats.normaltest(tips1['pct'])