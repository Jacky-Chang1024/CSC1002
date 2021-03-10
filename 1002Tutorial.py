#TUT4

# (Anagrams) Enter two different words and 
# check whether they are anagrams. Two words
# are anagrams if they contain the same letters.
# For example, silent and listen are anagrams.
# The program should print out in this way:
""" 
l1 = (input('Please enter the first word:'))
l2 = (input('Please enter the second word:'))

l11 = list(l1)
l22 = list(l2)
l11.sort()
l22.sort()
if l11 == l22:
    print('%s is an anagram of %s.'%(l1,l2)) 
"""
    
#list comprehension
# Use list comprehension to create a list containing 
# all the odd numbers smaller than 56.
""" 
s = list(range(1,57))
m =[x for x in s if x % 2 == 1]
print(m)


m = [x for x in range(26, 161) if (x % 4 == 0 and (x-6) % 10 == 0)]
print(m)
 """


        
        
# ( Prime) Ask the user to enter an integer N, and generate a list which contains all the prime
#number(s) smaller than N.
""" 
N = int(input('Please enter an integer n, n > 2: '))
s = list(range(2,N+1,1))
s1= list(range(2,N+1,1)) #这里设置两个list，因为如果一个的话不行
        #对于for，i是由地址得到，而remove后地址会改变（调试一下就明白了）
for i in s1:
    print('i=%d'%i)
    for j in range(2, int(i ** 0.5 //1 +2)) :#The square root of n , integer
        print('j=%d'%j)
        if i % j == 0:
            s.remove(i)
            break
s.insert(0,2)
print(s)
#print(s.insert(0,2))
 """

# (Ping-pong sequence) The ping-pong sequence counts up starting from 1 and is always
# either counting up or counting down. At element k, the direction switches if k is a multiple
# of 7 or contains the digit 7. The first five direction changes are after . The first 30 elements
# of the ping-pong sequence are listed below, with direction swaps marked using brackets at
# the 7th, 14th, 17th, 21st, 27th, and 28th elements
'''
n = int(input("Please enter a positive integer: "))
pingppng_list = [1] * n

direction = 1
for i in range(1, n):
    if i % 7 == 0 or str(i).find('7') != -1:
        direction = - direction
    pingppng_list[i] = pingppng_list[i-1] + direction
    
print("The %sth element in ping-pong sequence is: %s" % (n, pingppng_list[-1]))
'''


#TUT5

#A little bit tricky example to help you understand loop control.
#  What is the result? What if a = [0, 1, 2]?
'''
a = list(range(2))
for i in a:
    if i > 3:
        print(i)
        continue
else: #if 没有被执行的话，执行else
    print('There is no break in the if statement.')
'''

# Please remove all the "&nbsp" in this paragraph and capitalize each sentence. (Find the structure and
# take care of the spaces). (Hint: \n is used to split lines)

#diary = 
'''
at 10:30 am, Kinley sent me a pdf about String via &nbsp     kinley@cuhk.edu.cn.
at 12:15 pm, &nbsp     Xiaoming treated me a superb lunch as &nbsp     promised!
at 2:15 pm, Kinley asked me to give a &nbsp     quiz on my tutorial.
at 4:00 pm, &nbsp     Xiaoming sent the quiz questions via xiaoming@cuhk.edu.cn.
at 6:00 pm, a student told &nbsp     me he was &nbsp     desprate for a hard quiz!
'''


'''diary = diary.replace('&nbsp     ','')
diary = diary.split('\n')
out = ''
for i in diary:
    i = i.capitalize() + '\n'
     #注意capitalize是应用到整个句子的，所以
     #非内置默认大写的文字也会被变成小写
    out += i
print(out)'''
 
# Exercise 1
# As an example, suppose that the English word is scarm. Because the word begins with a consonant, you
# divide it into two parts, one consisting of the letters before the first vowel (i.e., a, e, i, o, u, A, E, I, O, U) and
# one consisting of that vowel and the remaining letters: scr am
# You then interchange these two parts and add ay at the end, as follows: am scr ay
# Thus the Pig Latin word for scram is amscray. For a word that begins with a vowel, such as apple, you simply
# add way to the end, which leaves you with appleway.
# If there is no vowel in this word, its Pig Latin is simply itself.

''' 
vowel = 'a e i o u A E I O U'
vowel = vowel.split()
##print(vowel)
k = 0
word = input()
wordList = list(word)
# for i in vowel:
#        if not word.find(i):
#        print(word)

for i in wordList:
    k += 1
    if i in vowel:
        break
    
L1 = wordList[0: k-1]
L2 = wordList[k-1:]
pigLatinList = L2 + L1 + list('ay')
#check whether there in no vowel
if pigLatinList == wordList + list('ay'): 
    print(word)
else:
    print(''.join(pigLatinList)) '''

# Prompt the user to input a series of different integers (more than 3) separated by single space and a target
# integer . Find three of these integers whose sum is closest to the target integer. Then print the sum of the
# three integers and those three integers. You may assume that each input would have exactly one solution.
# (hint: list, for loop)

''' 
l1 = input().split()
l = []

for i in l1:
    l.append(int(i))
    
tar = int(input())
N = len(l)
out = l[0]+l[1]+l[2] #初始值的设定

#print(N)
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            a = abs(l[i] + l[j] + l[k] - tar)
            #
            #print(i,j,k)
            if -a > -out:
                out = a
            else:
                continue
print(l[i],l[j],l[k])

 '''
 
 #TUT5

# Build a function called add_money , client can use this function to put money into the
# machine

def add_money(p_money, p_balance):
    g_money_list = [5,10,20,50,100]
    if p_money in g_money_list: 
        print
    else:
        print(" The machine only supports the money with 5, 10, 20, 50 or 100 face value. ")


# Create a goods list and a price list as global variable with the same length as below

goods_list = ['apple','orange','cola','juice','banana']
price_list = [3, 4, 5, 6, 4]

def show_goods():
    global goods_list
    global price_list
    print('%s%10s' %('Goods', 'Price'))
    for i in range(5):
        print('%-10s%d'%(goods_list[i] + ':', price_list[i]))

show_goods()

def buy_goods(p_balance, p_name, p_number = 1):
    global goods_list
    global price_list

    if p_name in goods_list:
        p_unit_price = price_list[goods_list.index(p_name)] 
        balance = p_balance - p_number * p_unit_price
        if balance >= 0:
            print('Buy successfully.')
            return balance
        else:
            print('Your money is not enough.')
            return p_balance
    else:
        print('No this term.')
        return p_balance

print('Your balance:', buy_goods(20,'appe',3))
print('Your balance:', buy_goods(20,'apple',3))


# 3. Reuse the functions in Q1 and Q2, then combine and invoke them to be a simple vending
# machine.

