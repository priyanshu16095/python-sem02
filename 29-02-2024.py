add = lambda x, y : x + y
result = add(2,3)
print(result)

# LSIT OF EVEN AND ODD N
def sumSquares(list):
    oddSquare = 0
    evenSquare = 0
    result = []
    for i in list:
        if i % 2 == 0:
            oddSquare += i*i
        else:
            evenSquare += i*i
    result.append(oddSquare)
    result.append(evenSquare)
    return result

# lambda argument : expression
# [expression for item in iterable if condition]

list1 = [1, 3, 5, 8]
squares = lambda lst : [sum(x*x for x in lst if x%2==0), sum(x*x for x in lst if x%2!=0)]
print(squares(list1))

def listSquares(lst):
    return [sum(x*x for x in lst if x%2==0), sum(x*x for x in lst if x%2!=0)]
print(listSquares(list1))

#  map(function, iterables)
y = 10
def fun(x):
    print(x)
    print(y)
fun(100)

a = 5
def s(a):
    print(a)
s(3)
print(a)

b = 5
def d():
    global b
    b = 15
d()
print(b)

def fact(num):
    fact = 1
    n = num
    while(n != 1):
        fact *= num
        n -= 1
        num -= 1
    print(fact)
fact(5)