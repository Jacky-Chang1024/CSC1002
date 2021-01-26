#   $Calculate  fractorial$
#from math import factorial
'''
print(factorial(5))       # output 120 = 5!
'''


#   $Nanmes and namespaces$
'''
n = 3 
employee = {
    'age': 45,
    'role': 'CTO',
    'SSN': 'AB1234567',
}
print(n)
print(employee)
'''
# n, employee are called name; a namespace is a mapping
# from names to objects
# For example, 
#from scipy.special import perm, comb 
# here the scipy.specail is a namespace.


#   $Scopes$
# a scope is a textual region of a Python program, 
# where a namespace is directly accessible.
# four types: local, enclosing, global, built-in
# the order scanned: LEGB
# NameError exception

'''
def local():
    m = 7
    print(m)

m = 5 
print(m)

# we call(execute) the function local
local() 

print(m)
'''

#consider the LEGB rule, 

'''
def local():
 #   m = 7      # here we remove m = 7
    print(m)

m = 5 
print(m)

# we call(execute) the function local
local() 

print(m)
'''

# more example:

'''
def enclosing_func():
    m = 13
    def local():
        print(m, 'printing from the local scope')

    local()

m = 5
print(m, 'printing from the global scope')

enclosing_func()
'''


#   $Object and classes$
# Classes are used to create objects, 
#objects are said to be instances of classes.

'''
class Bike:
    def __init__(self, colour, frame_material): 
        #pay attention that here __ is not _, 
        #being used as an initializer, called magic method
        self.colour = colour
        self.frame_material = frame_material 

    def brake(self):
        print("Braking!")

#let's create a couple of instances
red_bike = Bike('Red', 'Carnon fiber')
blue_bike = Bike('Blue','Steel')

print(red_bike.colour)
print(red_bike.frame_material)
print(blue_bike.colour)
print(blue_bike.frame_material)

red_bike.brake()
'''

#   $Guidelines on how to write good code$
print('hellko')
