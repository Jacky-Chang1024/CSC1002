# #这是基于python的luogu题解，未经本人允许禁止转载
# #https://www.luogu.com.cn/training/list

# # print(str(ord(input()) - 32))
# #为什么过不了。。。
# # print(input().upper())

# # x = input()
# # (a, b, c, d, e) = (x[4], x[3], x[2], x[1], x[0])
# # y = (a + b + c + d + e)
# # print(float(y))

# # t, n = input().split()
# # N = 2 * int(n)
# # V = float(t) / int(n)
# # print('%.3f\n%d'%(V,N))

# # a, b, c, d = input().split()
# # t_1 = int(a) * 60 + int(b)
# # t_2 = int(c) * 60 + int(d)
# # h, m = (divmod((t_2 - t_1), 60))
# # print(h, m)

# # a, b, c, d =map(int, input().split())


# # T = int(input())
# # if T == 1:
# #     print('I love Lougu!')
# # elif T == 2:
# #     print('%d %d'%(6,4))
# # elif T == 3:
# #     print('%d\n%d\n%d'%(3,12,2))
# # elif T == 4:
# #     print('%.3f'%(500/3))
# # elif T == 5:

# # a, b, c = map(float, input().split())
# # p = 0.5 * ( a + b + c)
# # s = ( p * (p - a) * (p - b) * (p - c)) 
# # s = s ** 0.5
# # print('%.1f'%s)

# # a, b = map(int, input().split())
# # m = a * 10 + b
# # n = m // 19 
# # print(n)

# # m, t, s = map(int, input().split())
# # if t == 0:
# #     x = 0
# # elif m > s / t:   
# #     if s % t == 0:
# #         x = m - s / t
# #     else:
# #         x = m - 1 - s // t
# # else:
# #     x = 0
# # print(int(x))

# # x = int(input())
# # print(x * (x-1) * (x-2) * (x-3) // 24 ) 
# # #整除用于保证输出整形

# # x = float(input())
# # a = bool(x % 2 == 0)
# # b = bool(4 < x <= 12)
# # if a and b :
# #     x1 = (1)
# # else:
# #     x1 = (0)
# # if a or b :
# #     x2 = (1)
# # else:
# #     x2 = (0)
# # if (a and not b) or (b and not a):
# #     x3 = (1)
# # else:
# #     x3 = (0)
# # if not a and not b:
# #     x4 = (1)
# # else:
# #     x4 = (0)
# # print(x1,x2,x3,x4)
# #python真的怎么写都行。。。

# # n = int(input())
# # if n % 100 == 0:
# #     if n % 400 == 0 :
# #         print(1)
# #     else:
# #         print(0)
# # elif n % 4 == 0:
# #     print(1)
# # else:
# #     print(0)

# # x = int(input())
# # if x > 1:
# #     a = str('s')
# # else:
# #     a = str()
# # print('Today, I ate %d apple%s.'%(x,a))
# #这里的%s的替换我觉着很妙

# # n = int(input())
# # a = 5 * n
# # b = 11 + 3 * n
# # if a < b:
# #     print('Local')
# # else:
# #     print('Luogu')

# #P5714
# # m, h = map(eval, input().split())
# # #print(m,h)
# # BMI = m / h ** 2
# # if BMI < 18.5:
# #     print("Underweight")
# # elif BMI >= 24:
# #     print("%.4f\nOverweight"%BMI)
# # else:
# #     print('Normal')

# # #P5715
# # a, b, c = map(int, input().split())
# # n = []
# # n.append(a)
# # n.append(b)
# # n.append(c)
# # n.sort()
# # print(n[0], n[1], n[2])
# # print(n)
    

# # #P5716
# # y, m = map(int, input().split())
# # if m == 1 or 3 or 5 or 7 or 8 or 10 or 12:
# #     print(31)
# # elif m == 4 or 6 or 9 or 11:
# #     print(30)
# # elif y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
# #     print(29)
# # else:
# #     print(28)
# # #不知道为什么不行
# #Copu the cript from @jimmy3246
# y, m = map(int, input().split())
# s = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
#     print(29)
#     else:
#     print(s[m])


