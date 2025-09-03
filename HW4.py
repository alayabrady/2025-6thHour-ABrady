#Name:Alaya Brady
#Class: 6th Hour
#Assignment: HW4


#1. Print Hello World!
print("hello world!")

#1. Create a list with 5 strings containing 5 different names in it.
cars_list=["Lightning McQueen", "Mater" , "Doc Hudson" , "Mack" , "Ramone"]
#2. Append a new name onto the Name List.
cars_list.append("Sally Carrera")
#3. Print out the 4th name on the list.
print(cars_list[3])
#4. Create a list with 4 different integers in it.
number_list=[23,22,45,12]
#5. Insert a new integer into the 2nd spot and print the new list.
number_list.insert(1,40)
print(number_list)
#6. Sort the list from lowest to highest and print the sorted list.
number_list.sort()
print(number_list)
#7. Add the 1st three numbers on the sorted list together and print the sum.
print(number_list[0] + number_list[1] + number_list[2])
#8. Create a list with two strings, two variables, and too boolean values.
mix_list=["eli","cars", 6, 7, True, False]
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(mix_list[int(input())])