# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces


# Create function - Comments used to define what function does. Convention is it starts with capital and ends with period
def sayHello():
    """
    Prints Hello and then name. 
    """
    print('Hello')

# Create function with parameter
def sayHello(name):
    print('Hello ' + name)

seyHello('Mohs')          # Call function

# Create function with default parameter
def sayHello(name='Beth'):
    print('Hello ' + name)

sayHello('Sam')           # Overwrites default parameter

# Return value
def getSum(num1, num2):
    total = num1 + num2
    return total

print(getSum(4,5))        # 9


def addOneToNum(num):
    num += 1
    return num

num = 5
new_num = addOneToNum(num)
print(new_num)            # 6

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2: num1 + num2     # do not need return statement
print(getSum(9,2))         # 11

addOneToNum = lambda num: num + 1
print(addOneToNum(11))     # 12