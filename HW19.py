#Name:alaya
#Class: 6th Hour
#Assignment: HW19

#1. Import the def functions created in problem 1-4 from HW16
from HW16 import hello_world, addition, animal_list ,loop
#2. Call the functions here and run HW19
hello_world()
addition(a=15, b=20 , c=32)
animal_list("orca","hammerhead shark","whale","sealion","seahorse")
loop(10)
#3. Delete all calls for problem 5 in HW16 and run HW19 again.

#4. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try:
    print(x)
except:
    print("hello world")
#5. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
try:
    num_div = int(input("give me an number: "))
    print(100/num_div)
except ZeroDivisionError:
    print("Cannot divide by zero!")

#6. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.

try:
    user_number = int(input("give me an number: "))
    print(f"your number is: {user_number}")
except ValueError:
    print("You didn't enter a number.")



#7. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
cnt=5
while True:
    if cnt <= 0:
        raise ValueError("can't below zero")
    print(cnt)
    cnt-=1