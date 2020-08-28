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

# m(m-1)/2
list = []
for m in range(1, 100):
    r = m*(m-1)/2 % 10
    list.append(r)
import matplotlib.pyplot as plt
plt.plot(list)
plt.title('m*(m-1)/2 % 10')

list = []
for m in range(1, 100):
    r = m%20*(m%20-1)/2 % 10
    list.append(r)
import matplotlib.pyplot as plt
plt.plot(list)
plt.title('m%20*(m%20-1)/2 % 10')

list = []
for m in range(1, 100):
    # r = 1%10+2%10+(m-1)%10  # 有问题
    # r = ( (int((m-1)/10)%10)*5 + (m%10)*((m-1)%10) / (2%10) )%10
    r = ((int((m - 1) / 10) % 10) * 5 + ((m - 1) % 10 + 1) * ((m - 1) % 10) / (2 % 10)) % 10
    list.append(r)
import matplotlib.pyplot as plt
plt.plot(list)
plt.title('1%10+2%10+(m-1)%10')


# 11^m的千分位中的百分位部分
from scipy.special import comb, perm
c_s = []
c1_s = []
c2_s = []
for m in range(1, 50):
    a = int(comb(m, 2))
    b = ( (comb(m, 1) - comb(m, 1)%10)/10 + comb(m, 2) ) % 10
    # a1: 为了消除差距而构造的
    a1 = (int(m/10) % 10 + comb(m, 2) % 10) % 10  # q + comb(m,2)

    # 对比个位数差异
    c = (a%10 - b%10)%-10
    c1 = (a1%10 - b%10)%-10
    c2 = -int(m/10)%-10

    c1_s.append(c1)
    c2_s.append(c2)
    c_s.append(c)
    print(m, a, b, c)
    print(a1, b)
    print('\n')
    # print(bin( int(a) ) ,bin( int(b) ))
import matplotlib.pyplot as plt
plt.clf()
plt.plot(c_s)
# plt.plot(c1_s)
plt.plot(c2_s)

# 11^m的千分位中的千分位
list = []
str_list = []
for m in range(4, 100):
    # r = m*(m-1)/2 % 10
    q = int(m / 10) % 10
    x0 = 1 # 1
    x1 = ((x0 - x0 % 10) / 10) + comb(m, 1)  # 10
    x2 = ((x1 - x1 % 10) / 10) + comb(m, 2)  # 100
    x3 = ((x2 - x2 % 10) / 10) + comb(m, 3)  # 1000
    x4 = ((x3 - x3 % 10) / 10) + comb(m, 4)  # 10000 # 记得改comb(m, 4)中的4

    r = x4  # input: 以谁为展示结果
    n = -5  # input: 对应第几项，-1为个位数
    list.append(r%10)
    str_list.append(int(str(11 ** m)[n]))
    print(m, str(int(r)%10), str(11 ** m)[n])
import matplotlib.pyplot as plt
plt.clf()
plt.plot(list)  # 通项公式数据
plt.plot(str_list)  # 真实结果数据

for m in range(4,20):
    r = 11**m
    print(r, str(r)[-4])





