import numpy as np
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
for i in range(50):
    P_H, P_A = prob_dict_HA[(S_1[-1], S_0[-1])]
    S_1.append(int(np.random.binomial(1, P_H)))
    S_0.append(int(np.random.binomial(1, P_A)))
print(S_0)

# -------------


def p_i(result, P_H_H_A, P_H_H_B, P_H_T_A, P_H_T_B, P_A):  # 输入实验结果，输出该实验结果的似然函数
    paras = {
        (1, 1): [P_H_H_A, P_A_H_A], (1, 0): [P_H_H_B, P_A_H_B],
        (0, 1): [P_H_T_A, P_A_T_A], (0, 0): [P_H_T_B, P_A_T_B]
    }
    if result == (1, 1):
        P = paras[result]
        # 累乘
        L = P_H_H_A*P_A + P_H_H_B*(1 - P_A)
        L = paras[(1, 1)][0]*P_A + paras[(1, 0)]*(1 - P_A)
    if result == (0, 1):
        L = P_H_T_A*P_A + P_H_T_B*(1 - P_A)
        L = paras[(0, 1)][0]*P_A + paras[(0, 0)]*(1 - P_A)
    if result == (1, 1, 1):
        L_1_1 = P_H_H_A*P_A + P_H_H_B*(1 - P_A)
        H_1_1
        L =

        return L

    def likelihood_function(P_H_H_A, P_H_H_B, P_H_T_A, P_H_T_B, P_A):
        return (P_H_H**H_H) * (P_H_T**H_T) * (1-P_H_H)**T_H * (1-P_H_T)**T_T

    return

p_i(1)




