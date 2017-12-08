#coding=utf-8
#第1,2课内容；
import numpy as np
import pandas as pd;
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import std
data =np.zeros(20);#生成一个包含20个0的一维数组
print data;
data =np.zeros((10,10));#生成一个10*10的矩阵
print data;
data =np.ones((5,5));#生成一个5*5的全是1的矩阵
print data;
data =np.eye(5);#生成一个5维的单位矩阵
print data;
data =np.arange(-5,5,0.1);#生成一个(-5,5),步长为0.1的数组
print data;
print data.dtype;#return data type
print data.shape;#return data size
print data.ndim;#return data 维度
data =np.arange(15);#生成包含15个数的一维数组
copy= np.copy(data);
print data[4];
slice =data[1:5];
print slice;
slice[3]=255;#slice 相当于指针
print data;
data =np.ones((5,5));
data1= np.dot(data.T,data);#矩阵的乘法
print data1;
copy1=np.add(copy,1);#任何运算函数可以作用在单个变量，也可以作用在数组的每一个元素上
print copy1;
print np.greater(copy,copy1);#比较两个矩阵中值的大小
data=np.linspace(0,10,100);#产生（0，10）之间100个元素的数组
print data;
data=np.meshgrid(15,15);#生成高维数组
print data;
a= np.where(5>3,5,3);#逻辑操作，等价于“5》3?5:3”
print a;
z= np.ones((3,4));
print z.sum(1);#求和一维行向量
print z.sum(0);#求和一维列向量
print np.unique(copy);#将数组中唯一的值合并到一个数组
from numpy.random import  rand;#random 包导入随机函数
x=rand(3,4);#均匀分布的随机数
print x;
from numpy.random import  randn;
x=randn(3,4);#标准正态分布随机函数
print x;
#例子：一只股票每日收益率为0.1%，每日波动率为0.5%，求100日后的预期收益率？
#由题设可知，这只股票服从u=0.1，σ=0.5的正态分布
mu =0.1;sigma=0.5;
#x服从N（0,1）→y=x*sigma+mu 服从N(mu,sigma^2);
x=randn(100);
y=sigma*x+mu;
print y.sum(0);
x=randn(100,100);#随机产生一百次的随机
y=sigma*x+mu;
print  np.average(y.sum(0),0);#平均收益率
y1=y.sum(0);
y1.mean(0);#期望
y1.std(0);#标准差













