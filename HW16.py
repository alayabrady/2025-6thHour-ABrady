#Name:Alaya
#Class: 6th Hour
#Assignment: HW16
import random


#1. Create a def function that prints out "Hello World!"
def hello_world():
    print("Hello World!")

#2. Create a def function that calculates the average of three numbers (set the 3 numbers as your arguments).
def addition(a,b,c):
    d=(a+b+c)/3
    print(d)

#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.
def animal_list(*fih):
    print("The 3rd animal is:", fih[2])



#4. Create a def function that loops from 1 to the number put in the argument.
def loop(water):
    for i in range (1,water+ 1):
        print(i)
#5. Call all of the functions created in 1 - 4 with relevant arguments.
hello_world()
addition(a=15, b=20 , c=32)
animal_list("orca","hammerhead shark","whale","sealion","seahorse")
loop(10)
#6. Create a variable x that has the value of 2. Print x
x=2
print(x)
#7. Create a def function that multiplies the value of 2 by a random number between 1 and 5.
def multix():
    global x
    x=x*random.randint(1,5)
multix()
#8. Print the new value of x.
print(x)


