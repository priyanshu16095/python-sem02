check1 = lambda n : n%2==0
print(check1(2))

check2 = lambda n : n>0 
print(check2(-1))

fun1 = lambda : print("Hello World")
fun1()

sum = lambda a,b : a+b
print(sum(2,3))

check3 = lambda a : print("{} is even".format(a)) if a%2==0  else print("{} is odd".format(a))
check3(5)

check4 = lambda a,b : print("{} is greater than {}".format(a,b)) if a>b else print("{} is less than {}".format(a,b))
check4(4, 5)

