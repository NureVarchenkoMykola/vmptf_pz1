# Task 1.1
i = 1
while i < 11:
    print (i)
    i += 1

# Task 1.2
# print(f"Hello {input('Enter your name: ')}")

# Task 2.1
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))

# average = (num1 + num2 + num3) / 3

# print(f"Average: {average}")

# Task 2.2
# numbers = list(range(1, 21))
# for num in numbers:
#     print(f"Number {num}, its square {num ** 2}")

# Task 3.1
# from datetime import date
# age = input("Enter your birth year: ")
# currentYear = date.today().year
# if age.isdigit():
#     birthYear = int(age)

#     if birthYear > currentYear or birthYear < 1900:
#         print("Enter your real birth year")
#     else:
#         age = currentYear - birthYear
#         print(f"Your age in {currentYear} is: {age}")
# else:
#     print("Error: Please enter digits only")

# Task 3.2
# def getOnlyEven (listOfNumbers):
#     evenList = []
#     for number in listOfNumbers:
#         if number % 2 == 0:
#             evenList.append(number)
#     return evenList

# myList = list(range(1, 21))
# result = getOnlyEven(myList)
# print(f"List with only even numbers: {result}")

# Task 4
# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def displayInfo (self):
#         print(f"Title: {self.title}\nAuthor: {self.author} \nYear: {self.year}")

# myBook = Book("Cobzar", "Taras Shevchenko", 1840)
# print("by using method of class:")
# myBook.displayInfo()

# print("\ndirect attribute access:")
# print(f"Title: {myBook.title}")
# print(f"Author: {myBook.author}")
# print(f"Year: {myBook.year}")