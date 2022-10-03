# a = [1,2,3,4,5]
# sum = 0
# for i in range(len(a)):
#     if (i % 2) != 0:
#         sum += a[i]
# print(sum)


# a = [1, 2, 3, 4, 5]
# b = []
# for i in range(round(len(a) / 2 + 0.01)):
#     b.append(a[i] * a[(-i) - 1])
# print(b)


# a = [1.1, 1.2, 3.1, 5, 10.01]
# max = a[1] % 1
# min = a[1] % 1
# for i in range(len(a)):
#     if a[i] % 1 == 0:
#         pass
#     elif max < (a[i] % 1):
#         max = a[i] % 1
#     elif min > (a[i] % 1):
#         min = a[i] % 1
# print(round((max - min), 3))


# a = int(input("Введите число: "))
# b = ''
# while a > 0:
#     b = str(a % 2) + b
#     a = a // 2
# print(b)


# fib1 = fib2 = 1
# b = [0, 1, 1]
# n = int(input())
#
# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     b.append(fib2)
# print(b)
#
# for i in range(n):
#     fib1 = (-1) ** i * b[(-n) + i]
#     b.insert(0, fib1)
# print(b)
