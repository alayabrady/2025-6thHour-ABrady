#Name:alaya
#Class: 6th Hour
#Assignment: HW18

import random
#1. Import the "random" library and create a def function that prints "Hello World!"
def hello_world():
    print("Hello World!")

#2. Create two empty integer variables named "heads" and "tails"
heads=0
tails=0
#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.
def coin_flip():
    global heads,tails
    for i in range(100):
        coin_flip_result = random.randint(1, 2)

        if coin_flip_result == 1:
            heads += 1
        else:
             tails += 1

#4. Call the "Hello world" and "Coin Flip" functions here
hello_world()
coin_flip()
#5. Print the final result of heads and tails here
print(heads)
print(tails)
#6. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanBag=["green beans","black beans","red beans","brown beans","yellow beans"]
#7. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def bean():
    random_bean=random.choice(beanBag)
    print(random_bean)
    beanBag.remove(random_bean)
    print(beanBag)
#8. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def bean_pull():
    question = str(input("do you want to pull beans? y/n"))
    if question == "y":
        bean()
        bean_pull()
    elif question == "n":
        print("Thank you for playing")
#9. Call the "Bean Pull" function here
bean_pull()
