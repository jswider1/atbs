# some functions and other stuff
# let's try handling an error
import random

def division(divide, by):
    try:
        return divide / by
    except:
        print('divided by zero or something...')

print(division(10,2))
print(division(12,0)) # None is what 12/0 gets when error is handled
print(division(8,3))

def howManyTrades():
    # getting trade first
    numTrades = None
    # loop for input
    while numTrades == None:
        try:
            numTrades = int(input('How many trades did you make today?: '))
            if numTrades < 0:
                print("Value must be zero or greater.")
                numTrades = None
            else:
                print(str(numTrades) + ' is okay.')

        except ValueError:  # ValueError try except block
            print('You did not enter a number.')
            
# call the function
howManyTrades()
print()

# some list stuff
print('Now making a list example...')
myList = ['what', 'the', 'ever', 'livin', 'are', 'you', 'doing']
print('This is my list: ')
print(myList)
newList = [['what', 'the', 'ever', 'livin', 'are', 'you', 'doing'], [1, 2, 3, 4, 5, 6, 7]]
print(newList)

