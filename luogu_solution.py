#这是基于python的luogu题解，未经本人允许禁止转载
#https://www.luogu.com.cn/training/list

# print(chr(ord(input()) - 32))
#为什么过不了。。。
# print(input().upper())

# x = input()
# (a, b, c, d, e) = (x[4], x[3], x[2], x[1], x[0])
# y = (a + b + c + d + e)
# print(float(y))

# t, n = input().split()
# N = 2 * int(n)
# V = float(t) / int(n)
# print('%.3f\n%d'%(V,N))

# a, b, c, d = input().split()
# t_1 = int(a) * 60 + int(b)
# t_2 = int(c) * 60 + int(d)
# h, m = (divmod((t_2 - t_1), 60))
# print(h, m)

# a, b, c, d =map(int, input().split())


# T = int(input())
# if T == 1:
#     print('I love Lougu!')
# elif T == 2:
#     print('%d %d'%(6,4))
# elif T == 3:
#     print('%d\n%d\n%d'%(3,12,2))
# elif T == 4:
#     print('%.3f'%(500/3))
# elif T == 5:

# a, b, c = map(float, input().split())
# p = 0.5 * ( a + b + c)
# s = ( p * (p - a) * (p - b) * (p - c)) 
# s = s ** 0.5
# print('%.1f'%s)

# a, b = map(int, input().split())
# m = a * 10 + b
# n = m // 19 
# print(n)

# m, t, s = map(int, input().split())
# if t == 0:
#     x = 0
# elif m > s / t:   
#     if s % t == 0:
#         x = m - s / t
#     else:
#         x = m - 1 - s // t
# else:
#     x = 0
# print(int(x))

# x = int(input())
# print(x * (x-1) * (x-2) * (x-3) // 24 ) 
# #整除用于保证输出整形

# x = float(input())
# a = bool(x % 2 == 0)
# b = bool(4 < x <= 12)
# if a and b :
#     x1 = (1)
# else:
#     x1 = (0)
# if a or b :
#     x2 = (1)
# else:
#     x2 = (0)
# if (a and not b) or (b and not a):
#     x3 = (1)
# else:
#     x3 = (0)
# if not a and not b:
#     x4 = (1)
# else:
#     x4 = (0)
# print(x1,x2,x3,x4)
#python真的怎么写都行。。。

# n = int(input())
# if n % 100 == 0:
#     if n % 400 == 0 :
#         print(1)
#     else:
#         print(0)
# elif n % 4 == 0:
#     print(1)
# else:
#     print(0)

# x = int(input())
# if x > 1:
#     a = str('s')
# else:
#     a = str()
# print('Today, I ate %d apple%s.'%(x,a))
#这里的%s的替换我觉着很妙