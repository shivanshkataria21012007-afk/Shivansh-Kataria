# Part 1: Basic Functions

def print_welcome():
    print('Welcome to Python Lab')


def greet_user(name):
    print(f'Hello {name}')


def add_two_numbers(num1, num2):
    return num1 + num2


def check_even_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


# Part 2: While Loop Practice

def print_numbers_while():
    i = 1
    while i <= 5:
        print(i)
        i += 1


def sum_until_zero():
    total = 0
    number = 1

    while number != 0:
        number = int(input('Enter a number (0 to stop): '))
        if number != 0:
            total += number

    print(f'Total: {total}')
    return total


def password_check():
    password = ''
    while password != 'admin123':
        password = input('Enter password: ')
        if password != 'admin123':
            print('Incorrect password. Try again.')
    print('Access granted')


def item_entry_system():
    total = 0
    item_name = ''

    while item_name.lower() != 'done':
        item_name = input("Enter item name ('done' to finish): ")
        if item_name.lower() == 'done':
            break

        quantity = int(input('Enter quantity: '))
        price = float(input('Enter price: '))
        total += quantity * price
        print(f'Added {item_name}: {quantity} x {price}')

    print(f'Total bill: {total}')
    return total


# Part 3: For Loop Practice

def print_numbers_for():
    for i in range(1, 11):
        print(i)


def total_from_list(list_numbers):
    total = 0
    for num in list_numbers:
        total += num
    return total


def print_items(items):
    for item in items:
        print(item)


def print_items_with_index(items):
    for index, item in enumerate(items):
        print(index, item)


# Part 4: Functions + Loops

def add_numbers_while(limit):
    total = 0
    i = 1
    while i <= limit:
        total += i
        i += 1
    return total


def calculate_total_for_loop(values):
    total = 0
    for value in values:
        total += value
    return total


# Example usage
if __name__ == '__main__':
    print_welcome()
    greet_user('Alice')
    print(add_two_numbers(5, 7))
    print(check_even_odd(8))

    print('\nTask 5: Print numbers 1 to 5 using while loop')
    print_numbers_while()

    print('\nTask 6: Sum numbers until 0')
    sum_until_zero()

    print('\nTask 7: Password check')
    password_check()

    print('\nTask 8: Item entry system')
    item_entry_system()

    print('\nTask 9: Print numbers 1 to 10 using for loop')
    print_numbers_for()

    print('\nTask 10: Calculate total from list [100, 200, 300]')
    numbers = [100, 200, 300]
    print(total_from_list(numbers))

    print('\nTask 11: Print items from list')
    print_items(['apple', 'banana', 'orange'])

    print('\nTask 12: Print items with index')
    print_items_with_index(['apple', 'banana', 'orange'])

    print('\nTask 13: Add numbers using while loop')
    print(add_numbers_while(5))

    print('\nTask 14: Calculate total using for loop')
    print(calculate_total_for_loop([10, 20, 30]))
