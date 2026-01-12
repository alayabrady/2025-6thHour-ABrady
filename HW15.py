#Name:Alaya Brady
#Class: 6th Hour
#Assignment: HW15

#1. import the "random" library
import random
#2. print "Hello World!"
print("Hello World!")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c=int(input("Enter another number: "))
#4. Add a and b together, then divide the sum by c. Print the result.
sum= a + b
print(sum)
e= sum / c
print(e)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
print(round(e))
#6. Create a list of five different random integers between 1 and 10.
list=[0,1,2,3,4]
print(list)
#7. Print the 4th number in the list.
print(list[4])
#8. Append another integer to the end of the list, also random from 1 to 10.
list.append(random.randint(1,10))
print(list)
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
list.sort()
print(list)
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i=1
while i <= 100:
    print(i)
    i+=i
#11. Create a list containing the names of five other students in the classroom.
names_list = ["greg", "devon", "ally" "kash", "eli"]
#12. Create a for loop that individually prints out the names of each student in the list.
names_list.sort()
print(names_list)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
i=1
while i<=100:
    if i* 10 == 0:
        continue
#14. Free space. Do something creative. :)
text="Do something creative"
reverse_text = text[::-1]
print(text)
print(reverse_text)