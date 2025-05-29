import math
import random

L=int(input("Enter lower limit : "))
U=int(input("Enter uper limit : "))
r=random.randint(L,U)
print("\nYou have only",round(math.log(U-L+1,2))," chances to guess!!!")
c=0;

while c<math.log(U-L+1,2):
    c+=1
    guess=int(input("Guess the number : "))
    if r==guess:
        print("Congratulations you win!!")
        break
    elif guess>r:
        print("Too High")
    elif guess<r:
        print("Too Low")
        
if c>math.log(U-L+1,2):
    print("\nThe number is : %d" % r)
    print("\tBetter luck next time!")
