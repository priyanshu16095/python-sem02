a = 5
if a < 10:
    print("a is less than 10")

age = 19 
if(age < 18):
    print("Not eligible")
else:
    print("Eligible")

# TERNARY OPERATORS
age = 19; message="Eligible"
if(age >= 18):
    print(message)
    print(type(message))
else:
    print("Not eligible to vote!")

marks = 85
if 80 < marks < 90:
    print('A grade')

if 0 < age <= 18:
    print("Not eligible to vote")
else:
    print(message)

list = [7, 8, 1, 2, 3]
for ele in list:
    print(ele)

for i in range(5):
    print(i)

L = [2, 4, 6, 8]
if all(x % 2 == 0 for x in L):
    print("All are even") 

x = 10
y = 12
if(x == 10 and y == 12):
    print("True")

