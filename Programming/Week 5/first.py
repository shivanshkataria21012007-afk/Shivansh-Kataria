fnnumber = int(input("Enter your fnum:"))
lnumber = int(input("Enter your lnum:"))
print(fnnumber + lnumber)


age=10
if(age>18):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

    marks=int(input("Enter your marks:"))
    if(marks>=90):
        print("Grade A")
    elif(marks>=75):
        print("Grade B")
    elif(marks>=50):
        print("PASS")
    else:
        print("FAIL")


#check given number is positive or negative
number=int(input("Enter a number:"))
if(number>0):
    print("Positive number")
else:
    print("Negative number")

temperature=int(input("Enter the room temperature:"))
if(temperature>30):
    print("It's a hot day.")
elif(temperature>20):
        print("It's a nice day.")
elif(temperature>10):
        print("It's a bit cold.")
else:
        print("It's cold.")

choice=int(input("Enter your choice:"))
match choice:
    case 1:
        print("Pizza")
    case 2:
        print("Burger")
    case 3:
          print("Pasta")
    case 4:
          print("Invalid choice")
days =int(input("Enter your choice:"))
match days:
    case 1:
          print("Monday")
    case 2:
          print("Tuesday")
    case 3:
          print("Wednesday")
    case 4:
            print("Thursday")
    case 5:
            print("Friday")
    case 6:
            print("Saturday")
    case 7:
            print("Sunday")

