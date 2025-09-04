#Name:Alaya
#Class: 6th Hour
#Assignment: HW5


#1. Create a list with 9 different numbers inside.
number_list=[12,23,34,56,78,90,13,24,57]
print(number_list)
#2. Sort the list from highest to lowest.
number_list.sort(reverse=True)
print(number_list)
#3. Create an empty list.
empty_list=[]
#4. Remove the median number from the first list and add it to the second list.
median=number_list[4]
empty_list.append(median)
empty_list.remove(median)
#5. Remove the first number from the first list and add it to the second list.
empty_list.append(number_list.pop(0))
#6. Print both lists.
print(number_list)
print(empty_list)
#7. Add the two numbers in the second list together and print the result.
apple=sum(number_list)
print(apple)
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
number_list.append(apple)
#9. Sort the first list from lowest to highest and print it.
number_list.sort()
print(number_list)