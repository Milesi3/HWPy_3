# a = '12 2 35 6 7'
# b = [int(i) for i in a.split()]
# print(max(b))
# print(min(b))
# import math
#
# a = 3.2
# b = -7.8
# c = 1
# d = b**2 - 4*a*c
# if d > 0:
#     x1 = (-b + math.sqrt(d)) / (2 * a)
#     x2 = (-b - math.sqrt(d)) / (2 * a)
#     print(x1, x2)
# elif d == 0:
#     x = -b / (2 * a)
#     print("x = %.2f" % x)
# else:
#     print("Корней нет")

# import math
# n = 8
# m = 4
#
# print((n * m) // math.gcd(n , m))


# a = 'one two one tho three one'
# a = a.split()
# for i in range(len(a)):
#     s = 0
#     for e in range(i):
#         if a[i] == a[e]:
#             s+=1
#     print(s, end=" ")

# a = []
# n = int(input())
# for i in range(n):
#     a.append(input().split(" "))
# z = input()
# for i in range(n):
#     if z == a[i][0]:
#         print(a[i][1])
#     elif z == a[i][1]:
#         print(a[i][0])


# a = 'apple orange banana banana orange'
# a = a.split()
# b = {}
# max = 0
# word = "zzzzzzzzzzzzzzzzzzz"
# for i in a:
#     b[i] = b.get(i,0) + 1
#     if (b[i] > max):
#             max = b[i]
#
# for elem in b:
#     if (b[elem] == max) and (elem < word):
#         word = elem
# print(word)

#
# sp = []
# d = {}
# for i in sp:
#     d[i] = d.get(i,0) + 1

sp = ['rr', 'tt','tt', 'tt', 'tt']
d = {}
# заполнение словаря
for i in sp:
    d[i] = d.get(i, 0) + 1
print(list(d.keys()))
print(list(d.values()))
print(d.items())
# перебор словаря
for key, val in d.items():
    print(key, val)
# сортировка словаря по значениям (по убыванию)
print(dict(sorted(d.items(), key=lambda x: -x[1])))
