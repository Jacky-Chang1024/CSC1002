import random as rd # to generate random numbers 

g_dimension = -1  
g_oneDArray = []
g_twoDArray = []  # represent the number structure
g_colum = -1  # represent g_colum coodinate in grid
g_row = -1  # represent row coodinate in grid
g_inversion = 0




def generate_g_oneDArray(p_dimension):
    '''generate a random array'''
    oneDArray = list((range(p_dimension ** 2)))
    rd.shuffle(oneDArray) 
    #convert 0 to space
    oneDArray[oneDArray.index(0)] = ' '
    return oneDArray

def find_g_inversion(p_oneDArray):
    '''find the g_inversion of the list'''
    inversion = 0
    oneDArrayWithoutSpace = [k for k in p_oneDArray]
    oneDArrayWithoutSpace.remove(' ')
    for i in range(g_dimension ** 2 - 1):
        for j in range(i + 1, g_dimension ** 2 - 1):
            if oneDArrayWithoutSpace[i] > oneDArrayWithoutSpace[j] : inversion += 1
    return inversion


def determine_solvability(p_inversion):
    '''check the solvability'''
    if g_dimension % 2 == 0:
        widthFromLast = g_dimension - (g_oneDArray.index(' ')) // g_dimension
        if (widthFromLast + p_inversion) % 2 == 1:
            return True
    elif g_dimension  % 2 == 1:
        if p_inversion % 2 == 0:
            return True
    else:
        return False


def print_g_twoDArray():
    '''print the g_twoDArray'''
    for i in range(g_dimension):
        for j in range(g_dimension):
            number = '{:' '^3}'.format(g_twoDArray[i][j])
            print(number,end='')
        print() #newline
    return


def determine():
    '''determine the outcome'''
    a1 = a2 = 0 #initialze
    for i in range(g_dimension):
        for j in range(g_dimension):
            a1 = g_twoDArray[i][j]
            if a1 > a2:
                a2 = a1
            elif i == g_dimension - 1 and j  ==  g_dimension - 1 and a1 == ' ' :
                    return True
            else:
                return False  #to exit nested loop
        

def operation_input():
    n1 = n2 = n3 = n4 = 1
    if g_colum == g_dimension - 1:
        n1 = 0
    if g_colum == 0:
        n2 = 0
    if g_row == g_dimension - 1:
        n3 = 0
    if g_row == 0:
        n4 = 0
    l = [upList[n1] , downList[n2] , leftList[n3] , rightList[n4]]
    l1 = []
    for i in l:
        if i != '0':
            l1.append(i)
    s = ', '.join(l1)
    operation = input('Enter your move (%s): ' %s)
    
    if operation == up:
        if g_colum == g_dimension - 1:
            print('Invalid input!')
        else:
            g_twoDArray[g_colum + 1][g_row], g_twoDArray[g_colum][g_row] = g_twoDArray[g_colum][g_row], g_twoDArray[g_colum + 1][g_row] 
            g_colum += 1
    elif operation == down:
        if g_colum == 0:
            print('Invalid input!')
        else:
            g_twoDArray[g_colum - 1][g_row], g_twoDArray[g_colum][g_row] = g_twoDArray[g_colum][g_row], g_twoDArray[g_colum - 1][g_row]
            g_colum -= 1        
    
    elif operation == left:
        if g_row == g_dimension - 1:
            print('Invalid input!')
        else:
            g_twoDArray[g_colum][g_row + 1], g_twoDArray[g_colum][g_row] = g_twoDArray[g_colum][g_row], g_twoDArray[g_colum][g_row + 1] 
            g_row += 1
    elif operation == right:
        if g_row == 0:
            print('Invalid input!')
        else:
            g_twoDArray[g_colum][g_row - 1], g_twoDArray[g_colum][g_row] = g_twoDArray[g_colum][g_row], g_twoDArray[g_colum][g_row - 1]
            g_row -= 1
    else:
        print('Invalid input!')
    return 0


def input_g_dimension():
    dimension = None  
    while dimension  == None:
        try:
            #get the dimension of the game
            dimension = int(input('Please enter the dimension of this game: '))
            if dimension >=3 and dimension <= 10:
                continue
            else:
                print('Invalid input! Please enter an integer n, 3 <= n <= 10!')
        except:
            print('Invalid input! Please enter an integer n, 3 <= n <= 10!')
        dimension = None
    return dimension


def convert_g_twoDArray(g_oneDArray):
    #convert the 1D array to a 2D array 
    twoDArray = [[0 for i in range(g_dimension)] for j in range(g_dimension)] 
    for i in range(g_dimension):
        for j in range(g_dimension):
            twoDArray[i][j] = g_oneDArray[i * g_dimension + j]   
    return twoDArray


criterion3 = 'n'
while criterion3 == 'n':
    
    g_dimension = input_g_dimension()

    criterion1 = 0
    while not criterion1:
        g_oneDArray = generate_g_oneDArray(g_dimension)
        g_inversion = find_g_inversion(g_oneDArray)
        criterion1 = determine_solvability(g_oneDArray)

    g_twoDArray = convert_g_twoDArray(g_oneDArray)

    #determine the coordinate of space
    g_colum = (g_oneDArray.index(' ')) // g_dimension
    g_row = (g_oneDArray.index(' ')) % g_dimension 

    #operation part
    right = None
    while right == None :
        try:
            up, down, left, right = input('''Enter the four letters used for up, down,
             left and right directions, sample: [u d l r] :''').split(' ')
        except:
            print('Invalid input!')
            right = None

    upList = ['0','up-' + up]
    downList = ['0','down-' + down]
    leftList = ['0','left-' + left]
    rightList = ['0','right-' + right]
    criterion2 = False
    moves = 0
    while not criterion2:
        print_g_twoDArray()
        operation_input()
        moves += 1
        if g_twoDArray[g_dimension - 1][g_dimension - 1] == ' ':
            criterion2 = determine()
    print_g_twoDArray()
    print('Congratulations! You solved the puzzle in %d moves!' %moves)

    criterion3 = input('Enter ‘n’ to start a new game or enter ‘q’ to end the game: ')




#1.不合法输入是否算到步数里？
#2.函数的变量参数问题