import numpy as np
from time import *
import sympy as smp
import time


def example():
    # 初始化
    x, y = smp.symbols('x y')

    # 表达式
    expr1 = smp.cos(x)
    expr2 = smp.exp(-x)
    expr3 = smp.exp(-x**2-y**2)

    # 求不定积分
    r1 = smp.integrate(expr1, x)

    # 求定积分
    r2 = smp.integrate(expr2, (x, 0, smp.oo))

    # 求多重积分
    r3 = smp.integrate(expr3, (x, -smp.oo, smp.oo), (y, -smp.oo, smp.oo))

    print("r1:", r1)
    print("r2:", r2)
    print("r3:", r3)


def example_f7():
    x1, x2, x3, x4, x5, x6, x7, x8 = smp.symbols('x1, x2, x3, x4, x5, x6, x7, x8')
    expr_f7 = x1+x2+x3+x4+x5+x6+x7+x8

    begin_time = time.time()
    test_result = smp.integrate(expr_f7, (x1,0,1), (x2,0,1), (x3,0,1), (x4,0,1), (x5,0,1), (x6,0,1), (x7,0,1), (x8,0,1))
    end_time = time.time()

    print('test_result: ', test_result)
    print('Comsumed time: ', end_time-begin_time)


# 与前一次结果相关，且有2个隐状态的硬币实验
np.random.seed(10)
# theta
P_H_H_A = 0.8; P_H_H_B = 0.3
P_H_T_A = 0.4; P_H_T_B = 0.1
P_A_H_A = 0.8; P_A_H_B = 0.4
P_A_T_A = 0.1; P_A_T_B = 0.2
prob_dict_HA = {
    (1, 1): [P_H_H_A, P_A_H_A], (1, 0): [P_H_H_B, P_A_H_B],
    (0, 1): [P_H_T_A, P_A_T_A], (0, 0): [P_H_T_B, P_A_T_B]
}

# initial
S_1 = [1]  # H:1, T:0
S_0 = [1]  # A:1, B:0

# generation
for i in range(7):
    P_H, P_A = prob_dict_HA[(S_1[-1], S_0[-1])]
    S_1.append(int(np.random.binomial(1, P_H)))
    S_0.append(int(np.random.binomial(1, P_A)))
results = S_1
print(results)


# -------------
P_H_H_A, P_A_H_A, P_H_H_B, P_A_H_B, P_H_T_A, P_A_T_A, P_H_T_B, P_A_T_B = \
    smp.symbols('P_H_H_A, P_A_H_A, P_H_H_B, P_A_H_B, P_H_T_A, P_A_T_A, P_H_T_B, P_A_T_B')
paras = {(1, 1): [P_H_H_A, P_A_H_A], (1, 0): [P_H_H_B, P_A_H_B],
         (0, 1): [P_H_T_A, P_A_T_A], (0, 0): [P_H_T_B, P_A_T_B]}

P_H, P_A = 1, 1
Matrices_p = [[P_H, P_A]]


for i in range(1, len(results)):
    last_coin_result = results[i - 1]
    last_probability = Matrices_p[i - 1]
    Matrices_p.append([paras[(last_coin_result, 1)][0] * last_probability[1] + paras[(last_coin_result, 0)][0] * (1 - last_probability[1]),
                       paras[(last_coin_result, 1)][1] * last_probability[1] + paras[(last_coin_result, 0)][1] * (1 - last_probability[1])])

L = 1
for i in range(len(results)):
    if results[i] == 1:
        L *= Matrices_p[i][0]
    elif results[i] == 0:
        L *= 1 - Matrices_p[i][0]
print(L)

begin_time = time.time()
result = smp.integrate(L, (P_H_H_A, 0, 1), (P_A_H_A, 0, 1),(P_H_H_B, 0, 1),(P_A_H_B, 0, 1),
                   (P_H_T_A, 0, 1),(P_A_T_A, 0, 1),(P_H_T_B, 0, 1),(P_A_T_B, 0, 1))
end_time = time.time()
print('result: ', result)
print('Consumed: ', end_time-begin_time)
