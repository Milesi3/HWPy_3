# d = 0.001
# x = 3.1415926535
# b = x % d
# z = b / d * 10 // 1
# if z >= 5:
#     print(x - b + d)
# else:
#     print(x - b)
import random


# def Factor(n):
#     Ans = []
#     d = 2
#     while d * d <= n:
#         if n % d == 0:
#             Ans.append(d)
#             n //= d
#         else:
#             d += 1
#     if n > 1:
#         Ans.append(n)
#     return Ans
# print(Factor(int(input())))


# a = [1,3,4,6,7,89,2,3,1]
# b = {}
# for i in a:
#     b[i] = b.get(i,0) + 1
# for key, val in b.items():
#     if val == 1:
#         print(key, end=' ')


# k = int(input())
# s = ""
# while k >= 0:
#     y = random.randint(0,100)
#     if y == 0:
#         y = ""
#     if k > 1:
#         s += str(y) +"x" +"^" + str(k) + "+"
#     elif k == 1:
#         s += str(y) +"x" + "+"
#     else:
#         s += str(y)
#     k-=1
#
# with open("file.txt", "w") as f:
#     f.write(s)
# print(s)


# import re
#
# with open('input01.txt', 'r') as f_i1, open('input02.txt', 'r') as f_i2, open('output.txt', 'w') as f_o:
#     x = re.split("x\^2 \+ |x \+ ", f_i1.read())
#     y = re.split("x\^2 \+ |x \+ ", f_i2.read())
#     if len(x) == len(y):
#         for i in range(len(x)):
#             x[i] = int(y[i]) + int(x[i])
#     f_o.write(str(str(x[0]) + 'x^2 + ' + str(x[1]) + 'x + ' + str(x[1])))

