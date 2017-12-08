#coding=utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import  Series,DataFrame
from scipy import  stats
tips=pd.read_csv('E:\webJRE\PyDemo1\\tips.csv');#载入文件
print tips.describe();#总体描述
print tips.dtypes;#DataFrame类型查看类型只是属性的形式，而4series采用dtype()方法
print tips[['sex','smoker','day','time']].describe();#对所选择的数据进行描述，pandas引用好几列的格式tips【【'列名1','列名2'】】
print tips['sex'].value_counts();#对于单列属性的引用，格式tips【'属性'】，同济某一个属性的取值可以用。value_counts()函数
#datafram索引
tips['sex'];#投影某一列
tips[0:3];#选择出从前三行
print tips.at[1, 'smoker']#选择出第一行，属性smoker的值
print tips.iat[1,1];#选择出第i+1行，j+1列的元素
print tips.loc[:,['sex','smoker']]#切片操作，:代表整个列表，被切分成sex和smoker两列
print tips.iloc[2:3,5:6]#被切的块儿行的取值范围（2,3），列的取值范围(5,6)
tips1=tips[:100];
print tips1
tips1=tips[200:];
print tips1
#datafram的合并
tips11=pd.concat([tips1,tips1]);#concat是个拼接函数，用于把多个·个datafram拼接成一个datafram 格式为pandas.concat([tips1,tips2，tips3])，按行合并
print tips11
left = DataFrame({'key':['wa','ha','ha'],'pwd':[123,456,789]})#用于生成每组属性对应多个属性值
print left
right = DataFrame({'key':['wa','ha','ha'],'no':[001,002,003]})#用于生成每组属性对应多个属性值
print pd.merge(left,right,on='key')#按列合并，只是个视图，除非赋给一个新的datafram变量，否则不会改变被合并两个datafram的数据结构
s1=tips.iloc[4];#选择出第四行
print s1
tips.append(s1);#只是返回一个新的datafram，并未改变原来tips的值
tips.append(s1,ignore_index=True)#让插入的一行元素在视图中按顺序显示
#datafram的合并
print tips.sort_values('tip');#改变当前视图的顺序，木有sort函数，只能使用sort_values函数
print tips
print tips[['total_bill','tip','size']].apply(lambda x:x.max()-x.min());#定义一个函数 并作用于每一列上，字符串不能做减法
#类别型变量
s=pd.Series(['a','b','c','a'],dtype='category')#生成一个category变量，第一种生成方式
print s.dtype;
s=pd.Series(['a','b','c','a'])#第二种生成方式
s_cat=s.astype('category', categories=['b','c','d'], ordered=True)#ordered 表示这个类别是否是有序的类别
print s_cat;
tips['sex']=tips['sex'].astype('category');#改变某一个属性的类别
print tips['sex'].dtype
print tips.dtypes;
print tips['sex'].describe()#类别型变量能用describe函数进行统计
print tips['sex'].cat.ordered#查询sex属性是否是有序的
tips['sex']=tips['sex'].cat.set_categories(['male','female'],ordered=True)#将sex属性转换成category变量的同时，按照male《female的大小进行排序
print tips['sex'].dtype;
tips['rate']=tips['tip']/tips['total_bill'];
print tips;
print pd.crosstab(tips.sex,tips.rate)
