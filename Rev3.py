#Name:alaya
#Class: 6th Hour
#Assignment: HW-R3

import random
#1. import random and print "Hello World!"
print("hello world")
#2. Create three variables that each randomly generate an integer between 1 and 10, print each number on the same line.
a =random_1=random.randint(1,10)
b =random_2=random.randint(1,10)
c =random_3=random.randint(1,10)
print(random_1,random_2,random_3)
#3. Create a list containing 5 strings listing 5 colors.
color_list=["red","blue","yellow","green","purple"]
#4. Use a function to randomly choose one of the 5 colors from the list and print the result.
print(random.choice(color_list))
#5. Create an if statement that determines which of the three variables from #2 is the lowest.
if a<= b and a<= c:
    print("a is the lowest number")
if b<= a and b<= c:
    print("b is the lowest number")
if c<= a and c<= b:
    print("c is the lowest number")
if a <= b and a <= c:
    print("they are equal")