# tutorials s*@%

print("I'm going to learn Python eventually.")
print("I'm Mindnumb, what is your name?")
# get your real n dude
thisDude = input()
print("Okay, let's hope you get it this time, " + thisDude + '?')
print("Dude, you got " + str(len(thisDude)) + " letters in your n.") # concatenate str (not "int")

print("Go ahead, store your age too, so everyone knows you're old?")
dudesAge = input()
print("Hopefully, you won't be " + str(int(dudesAge)+1) + " by the time you finish atbs.")

if thisDude == 'Justin':
    print('Dude, we are in an if.')
elif dudesAge < 37:
    print('Dude, you are at a lower level.')
elif dudesAge > 42:
    print('Dude, you are at a higher level.')
elif dudesAge > 60:
    print('Dude, you are at a master level.')

