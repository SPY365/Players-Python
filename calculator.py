# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("ক্যালকুলেটরটি Python ব্যবহার করে বানানো হয়েছে....!")
print("★★★★★★★★★★★★★★★★★★★★★★★★★★★★★")
print("ক্যালকুলেটরটি Coding করেছেন জিহাদ")
print("------------------------------‌‍!")
print("যে কোন একটি বাছাই করুন......")
print("--------------------------!")
print("1.যোগ")
print("2.বিয়োগ")
print("3.গুণণ")
print("4.ভাঁগ")

while True:
    # Take input from the user
    choice = input ("অপশন বাছাই করুন (1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("প্রথম সংখ্যাটি লিখুন: "))
        num2 = float(input("দ্বিতীয় সংখ্যাটি লিখুন: "))
        
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "×", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "÷", num2, "=", divide(num1, num2))
        break
    else:
        print("অনুগ্রহপূর্বক সঠিক অপশন/সংখ্যা বাছাই করুন....")