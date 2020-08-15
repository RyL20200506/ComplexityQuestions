# 与前一次结果相关，且有2个隐状态的硬币实验
import numpy as np
from time import *
# todo: fix seed
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
for i in range(250):
    P_H, P_A = prob_dict_HA[(S_1[-1], S_0[-1])]
    S_1.append(int(np.random.binomial(1, P_H)))
    S_0.append(int(np.random.binomial(1, P_A)))
print(S_1)
# -------------


# def likelihood(P_H_H_A, P_A_H_A, P_H_H_B, P_A_H_B, P_H_T_A, P_A_T_A, P_H_T_B, P_A_T_B):  # 输入实验结果，输出该实验结果的似然函数
def likelihood(P_H_H_A, P_A_H_A, P_H_H_B):  # 输入实验结果，输出该实验结果的似然函数
    # P_H_H_A = 0.5
    # P_A_H_A = 0.5
    # P_H_H_B = 0.5
    P_A_H_B = 0.5
    P_H_T_A = 0.5
    P_A_T_A = 0.5
    P_H_T_B = 0.5
    P_A_T_B = 0.5
    P_A = 1
    P_H = 1
    '''
    Prepare: result = [1, 1, 0, 0, 1]
    '''
    # parameters & theta
    paras = {(1, 1): [P_H_H_A, P_A_H_A], (1, 0): [P_H_H_B, P_A_H_B],
            (0, 1): [P_H_T_A, P_A_T_A], (0, 0): [P_H_T_B, P_A_T_B]}

    # history probability function
    Matrices_p = [[P_H, P_A]]
    '''
    P(S_01=H), P(S_00=A)
    P(S_11=H), P(S_10=A)
    P(S_21=H), P(S_20=A)
    P(S_31=H), P(S_30=A)
    ...
    '''

    for i in range(1, len(result)):
        # print(i)
        '''
        The probabiliry of (H,A) at the second time, 
        p_1_H = P(H|last_coin, A) * P(A) + P(H|last_coin, B) * (1-P(A))
        p_1_A = P(A|last_coin, A) * P(A) + P(A|last_coin, B) * (1-P(A))
        '''
        # Matrices_p.append([P_H_H_A * Matrices_p[i-1][1] + P_H_H_B * (1 - Matrices_p[i-1][1]),
        #                    P_A_H_A * Matrices_p[i-1][1] + P_A_H_B * (1 - Matrices_p[i-1][1])])
        # Matrices_p.append([paras[(1, 1)][0] * Matrices_p[i-1][1] + paras[(1, 0)][0] * (1 - Matrices_p[i-1][1]),
        #                    paras[(1, 1)][1] * Matrices_p[i-1][1] + P_A_H_B[(1, 0)][1] * (1 - Matrices_p[i-1][1])])
        last_coin_result = result[i-1]
        last_probability = Matrices_p[i-1]
        Matrices_p.append([paras[(last_coin_result, 1)][0] * last_probability[1] + paras[(last_coin_result, 0)][0] * (1 - last_probability[1]),
                           paras[(last_coin_result, 1)][1] * last_probability[1] + paras[(last_coin_result, 0)][1] * (1 - last_probability[1])])

    L = 1
    for i in range(len(result)):
        if result[i] == 1:
            L *= Matrices_p[i][0]
        elif result[i] == 0:
            L *= 1 - Matrices_p[i][0]
    return L


# testing likelihood function
result = [1, 1, 0, 0, 1]
def test():
    P_H_H_A = 0.4; P_H_H_B = 0.8
    P_H_T_A = 0.6; P_H_T_B = 0.3
    P_A_H_A = 0.1; P_A_H_B = 0.4
    P_A_T_A = 0.4; P_A_T_B = 0.7
    test_result = likelihood(P_H_H_A, P_A_H_A, P_H_H_B, P_A_H_B, P_H_T_A, P_A_T_A, P_H_T_B, P_A_T_B)
    print(test_result)


# calculate the integrate
from scipy import integrate
def bounds0():
    return [0, 1]
def bounds(*args):
    return [0, 1]
result = S_1
begin_time = time()
# test_result = integrate.nquad(likelihood, [bounds, bounds, bounds, bounds, bounds, bounds, bounds, bounds])
test_result = integrate.nquad(likelihood, [bounds, bounds, bounds])
end_time = time()

print(test_result)
print(end_time-begin_time)


def example_nquad():
    import scipy.integrate as integrate
    def f(x,y,z):
        return x*y*z
    def bounds_z():
        return [1, 2]
    def bounds_y(*args):
        return [2, 3]
    def bounds_x(*args):
        return [0, 1]
    result = integrate.nquad(f, [bounds_x, bounds_y, bounds_z])
    print(result)