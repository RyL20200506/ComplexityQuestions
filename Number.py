# 后继:
def successor(number):
    return number+1
# 加法
def addition(number_a, number_b):
    tmp=number_a
    for i in range(number_b):
        tmp=successor(tmp)
    return tmp
# 乘法
def multiplication(number_a, number_b):
    tmp=number_a
    for i in range(number_b-1):
        tmp=addition(tmp, number_a)
    return tmp
# 斐波那契
def fibonacci(number_a):
    tmp, plus_num = 0,1
    for i in range(number_a+1):
        tmp, plus_num = addition(tmp, plus_num), tmp
        yield tmp
list(fibonacci(11))

# test
n = 5
a_n = (1/6)*n*(n+1)*(n+2)
b_n = (1/2)*n*(n+1)
int(2**a_n*0.630882266676063396815526621896) % (2**b_n)

# test2
import numpy as np
def f(x):
    return 1/2 - (1/np.pi) * np.arctan(np.cos(np.pi*x)/np.sin(np.pi*x))
c = sum([np.math.factorial(i) * 10**(-i**3) for i in range(1, 100)])
n=3
10**(n**3-(n-1)**3) * f(10**((n-1)**3) * c) - f(10**(n**3) * c)


bin(10) # 10进制转2进制
int('0b1010',2) # 2进制转10进制

def minus_bi(a,b):
    return bin(int(a,2)-int(b,2))

def bi_mul(a,b):
    return bin(int(a, 2)*int(b, 2)+1)
bi_mul('1011','11')

#
eleven_s = [11**m for m in range(1, 200)]
N_2_eleven = [str(eleven_s[i])[-2] for i in range(len(eleven_s))]
import matplotlib.pyplot as plt
plt.figure()
plt.scatter(list(range(len(N_2_eleven))), N_2_eleven)

# colotz
# 验证公式: 3
n=4
m1 = 1
m2 = 0
p=2
r0 = 2**(n+m1) - 2**(m1) - (3**1)*2**(m2)
r1 = r0/(3**p)
print(r1)

# 验证公式: 7
n = 4
m1 = 3
m2 = 2
m3 = 1
m4 = 1
m5 = 0
p = 5
r0 = 2**(n+m1+m2+m3+m4+m5) - 2**(m1+m2+m3+m4+m5) - (3**1)*2**(m2+m3+m4+m5) - (3**2)*2**(m3+m4+m5) - (3**3)*2**(m4+m5) - (3**4)*2**(m5)
r1 = r0/(3**p)
print(r1)



'''
反解过程
n = 4
   ...:m1 = 3
   ...:m2 = 2
   ...:m3 = 1
   ...:m4 = 1
   ...:m5 = 0
   ...:p = 5
   ...:r0 = 2**(n+m1+m2+m3+m4+m5) - 2**(m1+m2+m3+m4+m5) - (3**1)*2**(m2+m3+m4+m5) - (3**2)*2**(m3+m4+m5) - (3**3)*2**(m4+m5) - (3**4)*2**(m5)
   ...:r1 = r0/(3**p)
   ...:print(r1)
7.0
bin((3**4)*2**(m5))
Out[35]: '0b1010001'
bin((3**3)*2**(m4+m5))
Out[36]: '0b110110'
minus_bi('100000000000','11010100101')
Out[37]: '0b101011011'
minus_bi('101011011','1010001')
Out[38]: '0b100001010'
minus_bi('100001010','110110')
Out[39]: '0b11010100'
minus_bi('11010100','100100')
Out[40]: '0b10110000'
minus_bi('100001010','10110000')
Out[41]: '0b1011010'
minus_bi('100001010','110000')
Out[42]: '0b11011010'
minus_bi('10110000','110000')
Out[43]: '0b10000000'
'''