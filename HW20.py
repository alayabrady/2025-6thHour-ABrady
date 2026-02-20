#Name: Alaya
#Class: 6th Hour
#Assignment: HW20

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class items:
    def __init__(self, stock, price, weight):
        self.stock=stock
        self.price=price
        self.weight=weight
    def pricedouble(self):
        self.price=self.price*2



#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
earrings=items(stock=67,price=67,weight=2)
rings=items(stock=67,price=67,weight=1)
necklace=items(stock=67,price=67,weight=4)
#3. Print the stock of all three objects and the cost of the second store item.
print(earrings.stock)
print(rings.stock)
print(necklace.stock)
print(rings.price)
#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
rings.pricedouble()
print(rings.price)
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
necklace.stock = 67 / 1/4
print(necklace.stock)
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del earrings
try:
    print("weight of earrings", earrings.weight)
except NameError:
        print("Error earrings no longer exists")