# n维积分
import numpy as np
from time import *
from scipy import integrate

# def likelihood(P_H_H_A, P_A_H_A, P_H_H_B, P_A_H_B, P_H_T_A, P_A_T_A, P_H_T_B, P_A_T_B):  # 输入实验结果，输出该实验结果的似然函数

# def f1(x1):  # 输入实验结果，输出该实验结果的似然函数
#     return x1
# def f2(x1, x2):  # 输入实验结果，输出该实验结果的似然函数
#     return x1*x2
# def f3(x1, x2, x3):  # 输入实验结果，输出该实验结果的似然函数
#     return x1*x2*x3
# def f4(x1, x2, x3, x4):  # 输入实验结果，输出该实验结果的似然函数
#     return x1*x2*x3*x4
# def f5(x1, x2, x3, x4,x5):  # 输入实验结果，输出该实验结果的似然函数
#     return x1*x2*x3*x4*x5
# def f6(x1, x2, x3, x4,x5,x6):  # 输入实验结果，输出该实验结果的似然函数
#     return x1*x2*x3*x4*x5*x6
# def f7(x1, x2, x3, x4,x5,x6,x7):  # 输入实验结果，输出该实验结果的似然函数
#     return x1*x2*x3*x4*x5*x6*x7

def f1(x1):  # 输入实验结果，输出该实验结果的似然函数
    return x1
def f2(x1, x2):  # 输入实验结果，输出该实验结果的似然函数
    return x1+x2
def f3(x1, x2, x3):  # 输入实验结果，输出该实验结果的似然函数
    return x1+x2+x3
def f4(x1, x2, x3, x4):  # 输入实验结果，输出该实验结果的似然函数
    return x1+x2+x3+x4
def f5(x1, x2, x3, x4,x5):  # 输入实验结果，输出该实验结果的似然函数
    return x1+x2+x3+x4+x5
def f6(x1, x2, x3, x4,x5,x6):  # 输入实验结果，输出该实验结果的似然函数
    return x1+x2+x3+x4+x5+x6
def f7(x1, x2, x3, x4,x5,x6,x7):  # 输入实验结果，输出该实验结果的似然函数
    return x1+x2+x3+x4+x5+x6+x7
def bounds(*args):
    return [0, 1]


test_result = integrate.nquad(f1, [bounds])
print('f1:', test_result)
test_result = integrate.nquad(f2, [bounds, bounds])
print('f2:', test_result)
test_result = integrate.nquad(f3, [bounds, bounds,bounds])
print('f3:', test_result)
test_result = integrate.nquad(f4, [bounds, bounds,bounds,bounds])
print('f4:', test_result)
test_result = integrate.nquad(f5, [bounds, bounds,bounds,bounds,bounds])
print('f5:', test_result)
test_result = integrate.nquad(f6, [bounds, bounds,bounds,bounds,bounds,bounds])
print('f6:', test_result)
test_result = integrate.nquad(f7, [bounds, bounds,bounds,bounds,bounds,bounds,bounds])
print('f7:', test_result)

