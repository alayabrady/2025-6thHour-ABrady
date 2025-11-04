#Name:alaya
#Class: 6th Hour
#Assignment: HW12

import random
#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
i=5
while i >= 1:
    print(i)
    i -= 1
else:
    print("Hello World")

#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
a=30
while a>0:
    if a%2==0:
        print(a)
    a-=1
print("done")
#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
w=30
while w>0:
    if w%3==0:
        print(w)
    w-=1
print("end")
#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
r= random.randint(1,6)
while r<=6:
    print(r)
    if r==1:
        break
    r=random.randint(1,6)
#5. Create a while loop that asks for a number input until the user inputs the n
ask=int(input("enter 0 to quit"))
while ask!=0:
    ask=int(input("enter 0 to quit"))
