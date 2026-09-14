#Part 1 basic functions

#TASK 1
def welcome():
    print("Welcome to Python Lab")

welcome()
#task 2
def hello(name):
    print("Hello", name)

hello("Paras Malik")
#task 3
def add(a, b):
    return a + b

print(add(9, 12))
#task 4
def check(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check(4))


#Part 2 while loop practice
#Task 5: Print numbers from 1 to 5
number = 1

while number <= 5:
    print(number)
    number = number + 1
#Task 6: Ask for numbers until 0, then print total
total = 0

number = int(input("Enter a number: "))

while number != 0:
    total = total + number
    number = int(input("Enter a number: "))

print("Total =", total)
#Task 7: Password check until correct
password = ""

while password != "admin123":
    password = input("Enter password: ")

print("Correct password!")
#Task 8: Item entry system and calculate total
total = 0

item = input("Enter item name: ")

while item != "0":
    price = float(input("Enter price: "))
    total = total + price

    item = input("Enter item name or 0 to stop: ")

print("Total =", total)
#Part 3: For Loop Practice
#Task 9: Print numbers from 1 to 10
for number in range(1, 11):
    print(number)
#Task 10: Calculate total from list [100, 200, 300]
numbers = [100, 200, 300]

total = 0

for number in numbers:
    total = total + number

print("Total =", total)

#Task 11: Print items from a list
items = ["Apple", "Milk", "Bread"]

for item in items:
    print(item)
#Task 12: Print items with index
items = ["Apple", "Milk", "Bread"]

for i in range(len(items)):
    print(i, items[i])

#Part 4: Functions + Loops
#Task 13: Function to add numbers using while loop
def add_numbers():
    total = 0
    number = int(input("Enter number: "))

    while number != 0:
        total = total + number
        number = int(input("Enter number: "))

    return total

print("Total =", add_numbers())
#Enter 0 to stop.
#Task 14: Function to calculate total using for loop
def calculate_total(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total

numbers = [100, 200, 300]

print("Total =", calculate_total(numbers))

#Task 15: Function to display items and prices
def display(items):
    for item in items:
        print(item[0], item[1])

items = [
    ["Apple", 2],
    ["Milk", 3],
    ["Bread", 4]
]

display(items)
#Part 5: Mini Assessment Practice
def add_items():
    items = []

    name = input("Enter item name or 0 to stop: ")

    while name != "0":
        price = float(input("Enter price: "))

        items.append([name, price])

        name = input("Enter item name or 0 to stop: ")

    return items


def calculate_total(items):
    total = 0

    for item in items:
        total = total + item[1]

    return total


def display(items):
    for item in items:
        print(item[0], "$", item[1])


# Main program

items = add_items()

display(items)

total = calculate_total(items)

print("Total =", total)