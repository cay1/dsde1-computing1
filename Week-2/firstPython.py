#message = 'If this has printed, you have run the code successfully.'
#print(message)

answer=input("enter a message: ")
print (answer)
num= int(input("enter a number between 1 and 10: "))
import random
x= random.randint(1,10)
if num>10 or num<1:
    print("invalid try again.")
    
elif x==num:
    print('TRUE')
else:
    print('FALSE')

cool 
