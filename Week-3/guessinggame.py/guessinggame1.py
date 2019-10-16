import random
x= random.randint(1,10)

#check if if statements work
print(x)

Chance=3
guess_status=True

while Chance>0 and guess_status== True:
    guess= int(input("I am thinking  of a number between 1 and 10. Guess my number: "))
    
    if guess>10 or guess<1 or type(guess)!=int:
        print("Invalid. Try again.")
        Chance= Chance-1
        #guess_status= False

    elif x==guess:
        print('CORRECT.')
        import sys
        sys.exit()
        break
        
    else:
        print('WRONG. TRY AGAIN')
        Chance= Chance-1

print("You ran out of guesses, the number was "+str(x)+".")

