#Name:Alaya.b
#Class: 6th Hour
#Assignment: HW6


#1. Import the "random" library
import random
#2. print "Hello World!"
print("hello world")
#3. Create three different variables that each randomly generate an integer between 1 and 10
d10=random.randint(1,10)
n10=random.randint(1,10)
j10=random.randint(1,10)
#4. Print the three variables from #3 on the same line.
print(d10 , n10, j10)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
d10+=2
n10-=4
j10*=1.5
#6. Print each result from #5 on the same line.
print(d10, n10, j10)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
rand_num_list=[random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
#8. Sort the list in #7 and print it.
rand_num_list.sort()
print(rand_num_list)
#9. Add together the highest three numbers in the list from #7 and print the result.
r=rand_num_list[1]+rand_num_list[2]+rand_num_list[3]
print(r)
#10. Create a list with 5 names of other students in this class and print the list.

#11. Shuffle the list in #10 and print the list again.

#12. Print a random choice from the list of names from #10.