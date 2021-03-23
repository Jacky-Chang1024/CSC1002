 #Question 1 (10% of this assignment)
'''
def sqrt(n):
    lastGuess, nextGuess = 1, 2
    while True:
        if abs(lastGuess-nextGuess) > 1e-5:
            lastGuess = nextGuess
            nextGuess = (lastGuess + n/lastGuess) / 2
        else:
            return nextGuess

N = int(input('Enter a positive number: '))
root =sqrt(N)
print('The approximation root of its square is : %.6f' %root) 
'''

#Question 2 (15% of this assignment)
'''
def isPrime(n):
    for j in range(2, int(n**0.5)+1):
        if n % j == 0:
            return False
    return True

def isPalindromic(n):
    s = str(n)
    s1 = s[::-1]
    if s == s1:
        return True
    else:
        return False

count = 0
num = 13
while count < 100:
    numInverse = int(str(num)[::-1])
    if isPrime(num) and isPrime(numInverse) and not isPalindromic(num):
        print('%5d' %num, end=" ")
        count += 1
        if count % 10 == 0:
            print()
    num += 1
'''

#Q3

'''
def getDigit(number):
    addValue = 0
    for i in str(number):
       addValue += int(i)
    return addValue

def sumOfDoubleEvenPalce(number):
    sum1 = 0
    snumber = str(number)
    for i in range(len(snumber)-2,-1,-2):
        doubleEven = 2*int(snumber[i])
        sum1 += getDigit(doubleEven)
    return sum1
        
def sumOfOddPlace(number):
    snumber = str(number)
    sum2 = 0
    for i in range(len(snumber)-1,-1,-2):
        sum2 += int(snumber[i])
    return sum2

def isValid(number):
    a = sumOfDoubleEvenPalce(number) + sumOfOddPlace(number)
    if a % 10 == 0:
        print("Valid")
    else:
        print('Invalid')


number = input('Please enter your card number: ')
isValid(number)

'''
'''
#Q4
def isAnagram(s1,s2):
    if len(s1) != len(s2):
        return "is not an anagram"
    else:
        l1, l2 = [], []
        for i in range(len(s1)):
            l1.append(s1[i])
            l2.append(s2[i])
        l1.sort()
        l2.sort()
        if l1 == l2:
            return "is an anagram"
        else:
            return "is not an anagram"

s1,s2 = input("Please enter two letter separated by space: ").split()
print(isAnagram(s1, s2))
'''

#Q5
'''
l = []
for i in range(100):
    l.append(False)
for i in range(100):
    for j in range(100):
        if (j+1) % (i+1) == 0:
            l[j] = not l[j]
print(l)
'''
#Q6

'''
l = [[' ' for i in range(8)] for j in range(8)] 
y = x = 0

def determine(y, x):
    for i in range(8):
        if l[i][x] == 'Q':
            return False

    for i, j in zip(range(y,-1,-1),range(x,8)):
        if l[i][j] == 'Q':
            return False
    
    for i, j in zip(range(y,-1,-1),range(x,-1,-1)):
        if l[i][j] == 'Q':
            return False
    return True

def printQueens():
    for i in range(8):
        for j in range(8):
            print('|' + l[i][j],end='')
        print('|')



cnt = 0       
while True:
    
    # if cnt == 92:
    #     break

    if y == 8:
        printQueens()
        # l[y-1][l[y-1].index('Q')] = ' '
        # y -= 2
        # x = l[y].index('Q') + 1
        # l[y][x-1] = ' '
        # cnt += 1
        break
        #If you want to print all posible solution, delete the break and 
        #cancle the comment before the break

    while x > 7:
        y -= 1
        x = l[y].index('Q')
        l[y][x] = ' '
        x += 1


    if determine(y,x):
        l[y][x] = 'Q'
        y += 1
        x = 0
    else:
        x += 1
'''        




    
