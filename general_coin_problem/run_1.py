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


def likelihood(P_H_H_A, P_H_H_B, P_H_T_A, P_H_T_B, P_A, P_H, result=[1, 1, 0, 0, 1]):  # 输入实验结果，输出该实验结果的似然函数
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
        print(i)
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
    return L, Matrices_p


test = likelihood(P_H_H_A=0.3, P_H_H_B=0.7, P_H_T_A=0.2, P_H_T_B=0.9, P_A=1, P_H=1, result=[1, 1, 0, 0, 1])





