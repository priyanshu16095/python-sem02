if True:
    print("Hello World")
if False:
    print("Hello World")
if None:
    print("Hello World")

if -12:
    print("-12")

if True:
    pass
else:
    print("Hello World")

a = 10
if a > 20:
    print("a is greater than 20")
elif a < 20:
    print("a is less than 20")
else:
    print("a is equal to 20")

b = 5
if b > 0:
    if b < 10:
        print("n is positive and less than 10")
    else:
        print("n is positive and is greater than 10")
else:
    print("n is a negative number")

p = 7; q = 6; r = 8
max = p
if(q > p and q > r):
    max = q
elif(r > p and r > q):
    max = r
print(max)

# WITHOUT WALRUS OPERATOR
n = 10
if n > 5:
    print(n)

# WITH WALRUS OPERATOR
if (n := 10) > 5:
    print(n)

mobileNo = "9027644034"
if(len(mobileNo) == 10):
    print("Thank Your :)")
else:
    print("Idiot, mobile number should be of 10 digits!")