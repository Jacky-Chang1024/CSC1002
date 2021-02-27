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
