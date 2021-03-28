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


#P1085

'''
# with open("test.txt", "r") as f:
#     data = f.read()
# print(data)
# data = data.split('\n')

x, y = [], []

for i in range(1,8):
    a, b = map(int, input().split())
    #a, b = map(int, data[i-1].split())
    x.append(a)
    y.append(b)

#print(x,y)
out = 0
for i in range(6,0,-1):
    if x[i] + y[i] > 8:
        out = i +1

print(out)
#print(list(range(6,-1,-1)))
'''

#P1909
'''
n = int(input())
l1,l2 = [],[]


for i in range(3):
    a,b = map(int, input().split())
    l1.append(a)
    l2.append(b)

import math #主要是这里取整的问题，要向上
money = math.ceil(n/l1[0])  * l2[0]
for i in range(1,3):
    n1 = math.ceil(n/l1[i])
    money1 = n1 * l2[i]
    if money1 < money:
        money = money1
print(money)

'''

#P1055

#l = input().split('-')
#s = str(l)
#print(l)
#print(s)
#b = ''.join(l)
#print(b)
#numL = []
'''
for i in l:
    numL.append(int(i))
for i in range()


'''

#P1055
'''
l = input()
s = ''.join(l.split('-'))
sums =0

for i in range(9):
    sums += (i + 1) * int(s[i]) 

rn = str(sums%11)
if rn == '10':
    rn = 'X'

if s[9]==rn:
    print('Right')
else:
    print(l[:12]+rn)
'''


#P1422 小玉家的电费
'''
s = int(input())
if s > 400:
    print('%.1f' % ((s - 400) * 0.5663 + 250 * 0.4663 + 150 * 0.4463))
elif s > 150:
    print('%.1f' % ((s - 150) * 0.4663 + 150 * 0.4463))
else:
    print('%.1f' % (s * 0.4463))
'''

#P1424 小鱼的航程
'''
x ,n = map(int,(input().split()))
cnt=0
for i in range(x,x+n):
    if (i) % 7 != 6 and (i) % 7 != 0:
        cnt+=1
print(cnt*250)   
'''

#P1888 三角函数
'''
l=list(map(int,input().split()))
l.sort()
for i in range(2,int(l[0]**0.5+1)):
    if l[0]%i == 0:
        if l[2]%i == 0:
            l[0]/=i
            l[2]/=i
print('%d/%d'%(l[0],l[2]))
'''


##找到了辗转相除法求最大公约数
'''
def gcd(x, y): # very fast
   return x if y == 0 else gcd(y, x%y)

print(gcd(40, 60))  # result: 20
'''

#P1002 [NOIP2002 普及组] 过河卒

bx,by,mx,my = map(int,input().split())

l=[[1 for i in range(by+2)] for j in range(bx+2)] #多创建1行用来防止超出index
for i in range(bx+2):
    l[i][by+1] = 0
for i in range(1,by+2):
    l[bx+1][i] = 0
#防止都变成零 所以从1开始

m1=[0,1,1,-1,-1,2,2,-2,-2]
m2=[0,2,-2,2,-2,1,-1,1,-1]
for i in range(9):
    if m1[i]+mx <= bx and m1[i]+mx >= 0 and m2[i]+my <= by and m2[i]+ my>= 0 :
        l[m1[i] + mx][m2[i] + my] = 0   

for i in range(bx+1):
    for j in range(by+1):
        if l[i][j]!=0 :
            l[i][j]=l[i-1][j]+l[i][j-1]
print(l[bx][by])




