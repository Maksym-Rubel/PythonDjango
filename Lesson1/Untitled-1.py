
# Task 1
print("-------------------Task 1----------------------")
def returnAge():
    BIRTH_YEAR = 2025
    user_input = input("Please enter birthday year: ")  
    age = BIRTH_YEAR - int(user_input)          
    print(f"You will be {age} years old in {BIRTH_YEAR}.")
returnAge()

# Task 2
print("-------------------Task 2----------------------")
def getYear():
    user_input = input("Please enter year: ")  
    if(int(user_input) % 4 == 0 and (int(user_input) % 100 != 0 or int(user_input) % 400 == 0)):
        print(f"{user_input} is a leap year.")
    else:
        print(f"{user_input} is not a leap year.")
getYear()

# Task 3
print("-------------------Task 3----------------------")
def calculateNumbers():
    total = 0
    num1 = int(float(input("Enter first number: ")))
    num2 = int(float(input("Enter second number: ")))
    for i in range(num1, num2 + 1):
        total += i
    print(f"The sum of numbers from {num1} to {num2} is: {total}")
calculateNumbers()


# Generators
# Task 1
print("-----------------Generators----------------------")
print("-------------------Task 1----------------------")
def evenNumbers(n1,n2):
    for i in range(n1, n2 + 1):
        if i % 2 != 0:
            yield i
for i in evenNumbers(1,10):
    print(i)
# Task 2
print("-------------------Task 2----------------------")
def listNum(lst, n1, n2):
    for i in lst:
        if i < n1 or i > n2:
            yield i


numbers = [1,2,3,4,5,6,7,8,9,10]
for i in listNum(numbers, 1, 5):
    print(i)