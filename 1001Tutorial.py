 # Tutorial 3
"""
# determine the differences
for i in range(5):
    print(i)
for i in range(1,5):
    print(i)
for i in range(5,1,-1):
    print(i)
#ragne -- list
r = range(5)
print(type(r))
l = list(r)
print(type(l))
print(r)
print(l)
# Break and Continue
# Try and expcept
 """


 # Q1
"""
a, b, c = map(float, input('Enter: ').split(',')) 

#不过这里a,b,c=eval(input("。。。"))就好。。。无语

print(a, b, c)
if b**2 - 4*a*c > 0:    
    x1 = 1/(2*a) * (-b + (b**2 - 4*a*c)**0.5)
    x2 = 1/(2*a) * (-b - (b**2 - 4*a*c)**0.5)
    print('x1=%.2f and x2=%.2f.'%(x1,x2))
elif b**2 - 4*a*c == 0:
    x1 = 1/(2*a) * (-b)
    print('x=%.2f.'%x1)
else:
    print('no real roots.')  """   

# Q2
"""
m, y = map(int, input('Enter the month and year: ').split(','))
l = [31,28,31,30,31,30,31,31,30,31,30,31]

dict = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',
7:'July',8:'August',9:'October',10:'November',12:'December'}

M = dict[m]

if y % 400 != 0 and  y % 4 != 0:
    d = l[m-1]
else:
    if m == 2:
        d = 29
    else: 
        d = l[m-1]
print('%s %d has %d days'%(M,y,d))  """

#Q3
""" 
while (1):

    n = input('Enter a number: ')
    l = list(n)
    a = len(l)
    i = 0
    c = 0
    while i < a:
        c = c + int(l[i])
        i += 1
    print(c)
    o = input('Do you want to continue? y or n:')
    if o == 'n':
        break
 """

 #Q4
""" 

#标答在这里用了
##Give an initial value other than 0
integer=None

##if integer==0, stop the loop
while integer != 0:       
    ##  Use try except to capture the error input 
    try:
        integer=int(input("Enter an integer, the input ends if it is 0:"))
    except:
        print("Invalid number!Please input again!")
        ##  Continue the loop while not execute the following code
        continue
    
来避免输入不合法字符使程序崩溃

(sum, p, n, i)= (0, 0, 0, 0)
while (1):
    a = int(input('Enter an interger, the input ends if it is 0: '))
    sum = sum + a
    if a > 0:
        p += 1
    elif a < 0:
        n += 1
    else:
        break
    i += 1
avg = sum / i
print('The number of positive is %d'%p)
print('The numer of negative is %d'%n)
print('The sum of numbers is %d'%sum)
print('The average of numbers is %.2f'%avg)
 """

 #Q5
'''


a = int(input())
i = 1
l = []
while (i):
    i += 1
    if a == 1:
        break
    elif a % i == 0:
        l.append(i)
        a = a / i
        i -= 1

print(','.join(str(j) for j in l))
#qPay attention to the requirment of output

标答要好的多
##Use try except to capture the error of not entering a number
try:
    integer=int(input("Enter an integer:"))
except:
    integer=None
    
if integer is None:
    print("The input is invalid!")
else:
    ##  Start from 2
    factor=2
    ##  Iterate from 2 to the integer
    while factor<=integer:             
        if integer%factor==0:
            ##  Stop when factor equal to the integer
            if integer==factor:         
                print(factor)
                break
            print(factor,end=',')
            integer/=factor
        else:
            factor+=1

#我只能说这个循环太妙了

'''

#Q6
'''
n = int(input())

for i in range(1,n+1):
    for j in range(1, n-i +1):
        print('  ',end='')
    for j in range(i,0,-1):
        print('%d '%j,end='')
    for j in range(2,i+1):
        print('%d '%j,end='')
    print('') 


#标答用不等式和定位来做好得多
for row in range(1,numOfLine+1):
        
    ##  Display the left part of the row
    for column in range(numOfLine,1,-1):
        if column<=row:
            ##  Print the number
            print("%4d"%column,end='')      
        else:
            ##  Print space
            print("%4s"%" ",end='')
            
    ##  Display the right part of the row
    for column in range(1,numOfLine+1):
        if column<=row:
            ##  Print the number
            print("%4d"%column,end='')      
        else:
            ##  Print space
            print("%4s"%" ",end='')
            
    ##  Change a new line to print
    print()



'''

