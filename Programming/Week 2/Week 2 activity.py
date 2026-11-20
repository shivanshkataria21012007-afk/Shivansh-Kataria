name = input("enter your name: ")
print(name)

age = input("enter your age: ")
print(age)

gpa = input("enter your gpa: ")
print(gpa)

local_student_status = input("enter your local student status: ")
print(local_student_status)

birth_year = input("enter your birth year: ")
print(birth_year)

current_year = 2026
age = current_year - int(birth_year)
print(f"age: {age}")
print(f"Student name: {name}") 
print(f"Student age: {age}")
print(f"Student gpa: {gpa}")
print(f"Student local student status: {local_student_status}")




product = input("enter your product name: ")
print(product)

price = input("enter your product price: ")
print(price)

quantity = input("enter your product quantity: ")
print(quantity)

subtotal = float(price) * int(quantity)
print(f"Subtotal: ${subtotal:.2f}")

gst_rate = 15
gst_amount = subtotal * gst_rate / 100
print(f"GST amount: ${gst_amount:.2f}")
final_total = subtotal + gst_amount
print(f"Final total: ${final_total:.2f}")


num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
print("Data type of first number:", type(num1))
print("Data type of second number:", type(num2))
num1 = int(num1)
num2 = int(num2)
print(f"Sum: {num1 + num2}")