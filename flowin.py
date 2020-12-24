# tutorials s*@%
import sys

print("I'm going to learn Python eventually.")
print("I'm Mindnumb, what is your name?")
# get your real n dude
thisDude = input()
if thisDude == 'Justin': 
    print("Thank you for sharing your name.")
else:
    print("You didn't enter Justin, you must be someone else.")

print("Okay, let's hope you get it this time, " + thisDude + '.')
print("Dude, you got " + str(len(thisDude)) + " letters in your n.") # concatenate str (not "int")

print("Go ahead, store your age too, so everyone knows you're old?")
dudesAge = int(input())
print("Hopefully, you won't be " + str(int(dudesAge)+1) + " by the time you finish atbs.")
# print(dudesAge)
# maybe do more if else statements later, lets speed things up
if thisDude == 'Justin':
    print('Dude, we just went in an if.')
elif dudesAge <= 37:
    print('Dude, you are at a lower level.')
elif dudesAge > 42:
    print('Dude, you are at a higher level.')
elif dudesAge > 60:
    print('Dude, you are at a master level.')

print("Okay, out of that loop. What do I want to do next...")
print("How about a while loop test.")

again = ''
while again != 'no':
    print("Want to stay in this while loop?")
    again = input()
    if again == 'n':
        print("That is just 'n', lazy, type 'no' to leave the while loop.")
print('Okay, out of that while loop.')

# just some play with while , if , and continue
gifts = 0
print(str(gifts))
while gifts < 4:
    gifts = gifts + 1
    print('In another while loop incrementing gifts')
    if gifts == 2:
        print('This if statement checks gifts and avoids output if gifts equals 2')
        continue
    print('which is now up to ' + str(gifts) + ' gifts.')

# okay now remembering for loops in Python
print('A loop to add a set of numbers within a specific range')
total = 0
for num in range(101):
    total += num
print(total)

print("pumping out counts with 'range' funtion.")
for i in range(0, 6, 2):
    print("count " + str(i) + ".")

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + ', so not exiting yet.')


