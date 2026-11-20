# Part 1: List Practice
numbers = [12, 25, 30, 45, 50]
print("List of numbers:")
print(numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])

numbers.append(60)
print("After append:", numbers)

numbers.insert(2, 99)
print("After insert at position 2:", numbers)

numbers.remove(30)
print("After removing 30:", numbers)

# Part 2: Tuple Practice
tuple_colors = ("red", "blue", "green", "yellow")
print("\nTuple colors:")
print(tuple_colors)
print("Second element:", tuple_colors[1])
print("Count of 'red':", tuple_colors.count("red"))

# Part 3: Dictionary Practice
student = {"name": "Alice", "age": 20, "city": "Auckland"}
print("\nStudent dictionary:")
print(student["name"])
print(student["age"])
print(student["city"])

student["course"] = "Programming 1"
print("After adding course:", student)

student["age"] = 21
print("After updating age:", student)

student.pop("city")
print("After removing city:", student)

# Part 4: For Loop Practice
print("\nNumbers from 1 to 10:")
for i in range(1, 11):
    print(i)

print("\nItems in a list using a loop:")
items = ["book", "pen", "eraser", "notebook"]
for item in items:
    print(item)

print("\nEven numbers only:")
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in num_list:
    if num % 2 == 0:
        print(num)

# Part 5: Logic Building
print("\nSum of numbers in a list:")
number_list = [10, 20, 30, 40, 50]
print(sum(number_list))

print("\nLargest number in a list:")
print(max(number_list))

# Part 6: Mini Project - Shopping Cart
print("\nShopping Cart")
shopping_cart = []
for i in range(3):
    item = input(f"Enter item {i + 1}: ")
    shopping_cart.append(item)

print("Your shopping cart items are:")
for item in shopping_cart:
    print(item)
