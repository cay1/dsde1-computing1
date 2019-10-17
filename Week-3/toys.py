'''
toys.py

Simple toy functions to get comfortable working 
with functions.
'''


# write a function that adds 1
# to the input and prints the result
a=int(input('enter a number:'))

def add_one (a):
    return a+1
    
print (add_one(a))

# write a function that adds
# the two input numbers together
# and returns the sum
b=int(input('enter a number:'))
def sum(a, b):
    return a+b
print (sum(a,b))


# write a function that takes two
# numbers, adds them together using 
# sum() and then increments the sum
# using inc_return
def sum_inc(a, b):
    return add_one(sum(a,b))
print (sum_inc(a,b))


# write a function that returns a 
# boolean (True or False) for whether 
# the input number is even
num_input=int(input('enter a number:'))
def is_even(num_input):
    if num_input%2==0:
        return True
    else:
        return False
print (is_even(num_input))


# create for loop that takes a string
# and an integer and returns a new string 
# that is the string repeated equal to 
# integer
# e.g. string_repeat('ho', 3) returns
# 'hohoho'

p = str(raw_input('input the word you want to repeat:'))
r = int(raw_input('how many times do you want it repeated?:'))
def string_repeat(p,r):
    # hint: you can add strings together 
    # in order to concatenate them
    product= p*r
    return product

print(string_repeat(p,r))

