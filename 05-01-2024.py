print("Hello World!")

# TYPE CHECKING
a = 5
print(type(a))
b = 4.5
print(type(b))

# OPERATORS
print(5*2)
print(5 // 2)
print(5 / 2)
print(5 % 2)
print(5 ** 2)
print(5 == 2)
print(5 < 2)
print(5 > 2)

# TAKING INPUT
name = input("Enter your name: ")
print(type(name))
rollno = int(input("Enter your rollno: "))
print(type(rollno))

# PROGRAM
print("---Enter the details---")
name = input("Name: ")
age = int(input("Age: "))
percentage = input("Percentage: ")
print("User Detials: ")
print("Name: ", name)
print("Age: ", age)
print("Percentage: ", percentage)

# PROGRAM
num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
print(num1 + num2)

# --------------------------------------------------

import keyword as kw
print(kw.kwlist)

""" This is a 
    Multiline comment. """

for i in range(5):
    print(i)
    print("Hello World!")

# IT WILL GIVE ERROR
# for i in range(5):
#     print(i)
# print(0)
#     print("Hello World!")

sum1 = 1 + 2 + 3 + \
      4 + 5 
print(sum1)

sum2 = (1 + 2 + 3 + 
      4 + 5)
print(sum2)

a = 10; b = 20; c = 30