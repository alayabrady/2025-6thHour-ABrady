#Name:alaya
#Class: 6th Hour
#Assignment: HW-R5

#1. Fix the "class" comment at the top to "6th Hour"

#2. Create a list of the names of all the students in the classroom.
names_list=["alaya","ally","devon","shane","ethan","greg","connor","tristan"]
#3. Create a for loop that prints the names of every student in the list.
for a in names_list:
    print(a)
#4. Using the "in" operator (hint: Google), create a for loop that only prints
#the name of a student if the letter "e" is in it.
for name in names_list:
    if "e" in name:
        print(name)