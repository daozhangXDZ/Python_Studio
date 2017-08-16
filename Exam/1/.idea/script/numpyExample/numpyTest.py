import numpy as np
a0 = np.array([1, 2, 3, 4]);
a1 = np.array([[1, 2], [3, 4]]);
print("------------numpy-------------------");
print("a0:");
print(a0);
print("a1:");
print(a1);
print("a0->[0]:");print(np.arange(1));
print("-----------间隔产生----------------");
'''在从1到3中产生9个数'''
print("在从1到3中产生9个数");
print(np.linspace(1,9,9));
print("-----------数组基础-----------------");
print("创建数组");
a = np.ones((2,2));
b = np.eye(2);
print(a);
print(b);
print("数组计算 >");
print(a > 2);
print("数组计算 ADD ");
print(a + b);
print("数组计算 SUB ");
print(a - b);
print("数组计算 MUI ");
print(a - b);
print("数组计算 DOT ");
print(b / a);
print("-----------数组统计-----------------");
print(a);
print(b);
print("数组求和");
print(a.sum());
print("数组列求和");
print(a.sum(axis=0));
print("数组列最小值");
print(a.min());
print("数组列最大值");
print(a.max());
print("数组边间");
print(np.floor(a));
print("矩阵");
print(np.dot(a,a));

