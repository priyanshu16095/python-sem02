import math

print(15 // 3)
print(-15 // 2)

radius = int(input("Enter the radius: "))
print(math.pi * radius * radius)

a = complex(input("Enter the num1: "))
b = complex(input("Enter the num2: "))
print(a + b)

name = ["Priyanshu", "Gupta"]
print(name[::-1])

lst = ['a', 'b', 'e']
tup = tuple(lst)
print(tup)

stu1 = {"Python" : 90, "Java" : 85, "C" : 75}
avg = (stu1["Python"] + stu1["Java"] + stu1["C"]) / 3
per = (avg / 300) * 100
print(per,"%")