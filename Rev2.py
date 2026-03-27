#Name:alaya
#Class: 5th Hour
#Assignment: HW-R2


#1. Print "Hello World!"
print("hello world")
#2. Create an empty list.
list=[]
#3. Create a list that contains the names of everyone in the classroom.
name_list=["ally", "devon", "alaya","conner","greg","tristan","shane","ethan","mr mack"]
#4. Print the list from #3, sort the list, then print the list again.
print(name_list)
name_list.sort()
print(name_list)
#5. Append 5 different integers into the empty list from #2 and print the list.
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)
print(list)
#6. Add together the middle three numbers in the list from #2 and print the result.
add=(2+3+4)
print(add)
#7. Remove the very first number in the list from #2. Print the new first number.
list.remove(1)
print(list)
#8. Create a dictionary with three keys with respective values: your name, your grade, and your favorite color.
alayaDict = {
    "name" : "alaya",
    "grade" : 9,
    "favortie color" : "purple",
}

#9. Using the update function, add a fourth key and value determining your favorite candy.
alayaDict.update({"favorite candy" : "rolo"})

#10. Print ONLY the values of the dictionary from #8.
print(alayaDict.values())