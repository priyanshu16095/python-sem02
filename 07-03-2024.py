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

list1 = [10, 101, 12, 14, 15, 18]

def sumOfDigits(nums):
    result = []
    for i in nums:
        current_sum = 0
        while i > 0:
            digit = i % 10
            current_sum += digit
            i = int(i / 10)
        result.append(current_sum)
    return result

def checkSum(nums):
    temp = sumOfDigits(nums)
    for i in temp:
        if i != 10:
            return False
    return True

arr = list(filter(checkSum, list1))
print(arr)

def isVowel(a):
    v = ['a', 'e', 'i', 'o', 'u']
    for i in a:
        for j in v:
            if i == j:
                return True
alphas = ['a', 'b', 'e', 'f', 'o', 'm', 'n', 'u']
vowels = list(filter(isVowel, alphas))
