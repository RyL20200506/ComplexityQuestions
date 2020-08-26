# Euclid Algorithm to solve clotze
# input: p
# output: progress

z = 9
p = 8  # 变成奇数时*3的次数
n = 1  #
coeffs_3 = [3**i for i in range(p)]  # constant
coeffs_2 = [0 for i in range(p)]  # variables to be solved
right_value0 = bin(3**p*z)[2:]
right_value1 = bin(2**(len(bin(3**p*z)[2:])+n))[2:]  # n表示重复迭代的次数
right_value = bin( int(right_value1,2) - int(right_value0,2) )[2:]  # 表示等式右边待fit的值
print(right_value, int(right_value,2))

# Euclid Algorithm
for i in range(-1, -len(coeffs_3)-1, -1):
    print(i)
    print('original value',right_value)
    assert right_value[0] != 'b'  # 不能为负数
    if right_value[-1]=='1':  # it is odd
        coeffs_2[i]=0
    else:  # it is even: 值为右边0的个数
        right_1_idx = right_value.rfind('1')  # 最小的1的位置
        right_0_num = len(right_value) - right_1_idx - 1  # 最右边有几个0
        coeffs_2[i]=right_0_num
    # 更新right_value
    right_value_new = bin( int(right_value,2) - coeffs_3[i]*2**coeffs_2[i] )[2:]
    print('减数：', bin(coeffs_3[i]*2**coeffs_2[i])[2:])
    # print('2的指数(10-Hex)：',coeffs_2[i]),
    # print('3^p(2-hex)：',bin(coeffs_3[i])[2:])
    right_value = right_value_new
    print('new value',right_value_new,'\n')

assert right_value=='0'  # 化简失败

# Summary
print('故:'+'2**'+str(len(bin(3**p*z)[2:]))+'-'+'3**'+str(p)+'*'+str(z)
      +'\n='+str(int(right_value1,2))+'-'+str(int(right_value0,2)) + '             ---10Hex'
      +'\n='+str(bin( int(right_value1,2)- int(right_value0,2) ))[2:] + '             ---2Hex'
      +'\n='+'sum of '+str([str(coeffs_3[j])+'*2**'+str(coeffs_2[j]) for j in range(len(coeffs_3))])+ '             ---10Hex'
      +'\n='+str(bin(sum([coeffs_3[j]*2**coeffs_2[j] for j in range(len(coeffs_3))]))[2:])+ '             ---2Hex'
      +'\n='+str(sum([coeffs_3[j]*2**coeffs_2[j] for j in range(len(coeffs_3))]))+ '             ---10Hex')
print(coeffs_2)


#
def mod(a,b):
    print(a/b, a%b)