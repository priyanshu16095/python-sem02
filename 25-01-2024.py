print("Aaj Surprise test ho gaya")

list = [10, 20, 30, 40]

# WHILE LOOP
i = 0
while i < len(list):
    print(list[i])
    i += 1
else:
    print("Condition False")

j = sum = 0
while j  < len(list):
    sum += list[j]
    j += 1
print(sum)

k = 0
while k < len(list):
    if(list[k] % 2 == 0):
        print("Even number is {}".format(list[k]))
    else:
        print("Odd number is {}".format(list[k]))
    k += 1

# FOR LOOP
for i in list:
    print(i)

l = add = 0
for l in list:
    add += l
    l += 1
print("Sum is {}".format(add))

for i in range(5):
    print(i)

for j in range(1, 5):
    print(j)

for k in range(1, 50, 4):
    print(k)

for l in range(1, 10):
    if(l % 2 != 0):
        print(l)

num = 6
for m in range(1, 11):
    print("{} * {} = {}".format(num, m, num * m))