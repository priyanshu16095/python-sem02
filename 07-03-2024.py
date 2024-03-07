num1 = 10
num2 = 0
try:
    result = num1 / num2
except ZeroDivisionError:
    print("Cannot divide by zero! idiot!")
except Exception:
    print("Something went wrong")
else:
    print(result)
finally:
    print("Thank you! :)")

nums = [10, 101, 12, 14, 15, 18]

def sumOfDigits(nums):
    result = []
    for i in nums:
        sum = 0 
        while(i > 0):
            digit = i % 10
            sum += digit
            i = (int) (i / 10)
        result.append(sum)
    return result

result = sumOfDigits(nums)
print(result)

def checkSum(nums):
    temp = sumOfDigits(nums)
    for i in temp:
        if i == 10:
            return True
        else:
            return False

arr = list(filter(checkSum, nums))
print(arr)