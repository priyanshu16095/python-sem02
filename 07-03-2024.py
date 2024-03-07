num1 = 10
num2 = 5
try:
    result = num1 / num2
except ZeroDivisionError:
    print("Cannot divide by zero! idiot!")
except Exception:
    print("Something went wrong")
else:
    print(result)
finally:
    print("No exception occured :)")