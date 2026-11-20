# arithmetic operators
#Task 1
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Division:", b / a)
print("Multiplication:", a * b)

#Task 2 
a = int(input("Enter a number: "))
print("remainder:", a % 2)
print("floor division:", a // 2)

#Comparison Operators
#Task 3
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)
#task 4
age = int(input("Enter your age: "))
if age <= 12:
    print("child ticket.")
elif age >= 60:
    print("senior citizen ticket.")
else:
    print("adult ticket.")

    #Part 4 – Assignment Operators
    #Task 5
salary = 3000
salary += 500
salary *= 2
print("Final salary:", salary)

#Task 6

user_name= ("'john', 'maria', 'alex', 'sam'")
user_name_entered_by_user = input("Enter a username to check: ")

if user_name_entered_by_user in user_name:
    print("Username exists in the list.")
else:
    print("Username does not exist in the list.")
    #task 7
x = 10
y = 10

print("x is y:", x is y)
print("x == y:", x == y)
print("== checks whether two variables have the same value, while 'is' checks whether two variables refer to the same object in memory")

#Task 8
student_marks = int(input("Enter the student's marks: "))
if student_marks >= 50:
    print("Pass.")
elif student_marks < 50:
    print("Fail.")

#Task 9
print("= is the assignment operator — it stores a value in a variable (e.g. x = 5 puts 5 into x). == is the comparison operator — it checks whether two values are equal and returns True or False. The modulus operator (%) finds the remainder of a division. The and operator combines two conditions and only returns True if both conditions are true. If either one is false, the whole expression is False. // divides two numbers and rounds the result down to the nearest whole number.")