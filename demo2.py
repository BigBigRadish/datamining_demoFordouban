#coding=utf-8
import numpy as np
import pandas as pd
from pandas import  Series,DataFrame
s=Series([1,2,3],index=['a','b','c'])#一列属性，一列值
print s;
print np.max(s);
s.name='rank'
s.index.name='name'
print s;
sdata1={'name':['a','b','c'],'rank':[1,2,3],'score':[98,97,96]}
df1=DataFrame(sdata1)
print df1;
print df1.columns;#打印出每一个属性
df2=DataFrame(sdata1,columns=['score','rank','name'])#调整吗每列顺序
print df2;
df3=DataFrame(sdata1,columns=['score','rank','name','class'],index=['1','2','3']);#自动补全缺失值
print df3;
df3.reindex(['1','2','3','4'])#reindex（）新加一行
print df3;
print df3['score'];#投影当前属性的一列元素
print df3.ix['1'];#按行索引
print df2[df2['score']>60]#返回属性值大于60的所有元组；
del df3['class'];#会改变列表的数据结构
print df3;#删除某列
print df3.T;#转置
df3.reindex(['0','1','2','3'])#自动填充index
print df3;
df3.reindex(['0','1','2','3'],method='bfill')#向后填充新增的一行
print df3;
df3.drop('1');#丢掉index对应的那一行
print df3.drop('1');#drop只是显示的时候会丢掉，但并不会改变列表的数据结构
print df3.drop('score',axis=1)#丢掉score对应的那一列，axis=0，表示按行，axis=1，表示按列0
tips=pd.read_csv('E:\webJRE\PyDemo1\\tips.csv');#读取文件,自动变成一个DATAfram，并自动生成index
print tips;
print tips.head(6);#列出前n行
print tips.tail(7);#列出最后n行
tips1=pd.read_table('E:\webJRE\PyDemo1\\tips.csv',sep=',');#按表格格式读入，sep是指出数据分隔符
#print tips1.head(10);
#tips2=pd.read_table('E:\webJRE\PyDemo1\\douban.dat',sep='::');#按表格格式读入，sep是指出数据分隔符
#print tips2.head(10);
#print tips2.tail(7);#列出最后n行
print tips1.dtypes;#注意不是dtypes（）函数，这个函数只有series对象中有
print tips.describe();#列出数据总的特征，包括总数，标砖差，平均数等，中位数往往比平均数更抗噪