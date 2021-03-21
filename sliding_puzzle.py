#这是2020-2021春CUHKSZ的CSC1002作业 Sliding Puzzle
#这不是我的最终代码，仅提供一份思路来解决问题



import random as rd # to  random numbers 

dimension = 0
iSpace = 0
jSpace = 0

# a random array
def _oneDArray():
    global oneDArray
    oneDArray = list((range(dimension ** 2)))
    rd.shuffle(oneDArray) 
    #convert 0 to space
    oneDArray[oneDArray.index(0)] = ' '


#find the inversion of the list
def find_inversion():
    global inversion
    inversion = 0
    oneDArrayWithoutSpace = [k for k in oneDArray]
    oneDArrayWithoutSpace.remove(' ')
    for i in range(dimension ** 2 - 1):
        for j in range(i + 1, dimension ** 2 - 1):
            if oneDArrayWithoutSpace[i] > oneDArrayWithoutSpace[j]:
                inversion += 1

#check the solvability
def determine_solvability():
    #print(widthFromLast)
    if dimension % 2 == 0:
        widthFromLast = dimension - (oneDArray.index(' ')) // dimension
        if (widthFromLast + inversion) % 2 == 1:
            return True
    elif dimension  % 2 == 1:
        if inversion % 2 == 0:
            return True
    else:
        return False
        #  if ( dimension - ((oneDArray.index(' ') + 2)  % dimension)) % 2  == 1


def print_twoDArray():
    '''print the twoDArray'''
    for i in range(dimension):
        for j in range(dimension):
            number = '{:' '^3}'.format(twoDArray[i][j])
            print(number,end='')
        print() #newline
    return



def determine():
    '''determine the outcome'''
    a1 = a2 = 0 #initialze
    for i in range(dimension):
        for j in range(dimension):
            a1 = twoDArray[i][j]
            if i == dimension - 1 and j  ==  dimension - 1 and a1 == ' ' :
                return True
            elif a1 > a2:
                a2 = a1
            else:
                return False  #to exit nested loop
        

def operation_input():
    global iSpace
    global jSpace
    n1 = n2 = n3 = n4 = 1
    if iSpace == dimension - 1:
        n1 = 0
    if iSpace == 0:
        n2 = 0
    if jSpace == dimension - 1:
        n3 = 0
    if jSpace == 0:
        n4 = 0
    l = [upList[n1] , downList[n2] , leftList[n3] , rightList[n4]]
    if '' in l:
        l.remove('')
    s = ', '.join(l)
    operation = input('Enter your move (%s): ' %s)
    
    if operation == up:
        if iSpace == dimension - 1:
            print('Invalid input!')
        else:
            twoDArray[iSpace + 1][jSpace], twoDArray[iSpace][jSpace] = twoDArray[iSpace][jSpace], twoDArray[iSpace + 1][jSpace] 
            iSpace += 1
    elif operation == down:
        if iSpace == 0:
            print('Invalid input!')
        else:
            twoDArray[iSpace - 1][jSpace], twoDArray[iSpace][jSpace] = twoDArray[iSpace][jSpace], twoDArray[iSpace - 1][jSpace]
            iSpace -= 1        
    
    elif operation == left:
        if jSpace == dimension - 1:
            print('Invalid input!')
        else:
            twoDArray[iSpace][jSpace + 1], twoDArray[iSpace][jSpace] = twoDArray[iSpace][jSpace], twoDArray[iSpace][jSpace + 1] 
            jSpace += 1
    elif operation == right:
        if jSpace == 0:
            print('Invalid input!')
        else:
            twoDArray[iSpace][jSpace - 1], twoDArray[iSpace][jSpace] = twoDArray[iSpace][jSpace], twoDArray[iSpace][jSpace - 1]
            jSpace -= 1
    else:
        print('Invalid input!')
    return 0

criterion3 = 'n'
while criterion3 == 'n':
    #get the dimension of the game
    dimension = int(input('Please enter the dimension of this game: '))


    criterion1 = 0
    while not criterion1:
        _oneDArray()
        find_inversion()
        criterion1 = determine_solvability()

    #convert the 1D array to a 2D array 
    twoDArray = [[0 for i in range(dimension)] for j in range(dimension)] 
    for i in range(dimension):
        for j in range(dimension):
            twoDArray[i][j] = oneDArray[i * dimension + j]   
    #print(twoDArray)


    #determine the coordinate of space
    iSpace = (oneDArray.index(' ')) // dimension
    jSpace = (oneDArray.index(' ')) % dimension 

    #operation part
    up, down, left, right = input('Enter the four letters used for up, down, left and right directions, sample: [u d l r] : ').split(' ')
    upList = ['','up-' + up]
    downList = ['','down-' + down]
    leftList = ['','left-' + left]
    rightList = ['','right-' + right]
    criterion2 = False
    moves = 0
    while not criterion2:
        print_twoDArray()
        operation_input()
        moves += 1
        if twoDArray[dimension - 1][dimension - 1] == ' ':
            criterion2 = determine()

    print('Congratulations! You solved the puzzle in %d moves!' %moves)

    criterion3 = input('Enter ‘n’ to start a new game or enter ‘q’ to end the game: ')

