myString = "Hello"
print(myString[2])
print(myString[2:5])

for c in myString:
    print(c)

s1 = "Priyanshu"
s2 = "Gupta"
s3 = s1 + s2
s4 = s1 * 3

count = 0
for i in myString:
    if(i == "l"):
        count += 1
print(count)

print('l' in 'Hello World') #STRING MEMBERSHIP TEST

s5 = "The quick brown fox jumps over the lazy dog. How are you?"
vowelCount = {}
l = ['a', 'e', 'i', 'o', 'u']
for i in s5:
    for j in l:
        if(i == j):
            print("{} is at index: {}".format(i, s5.index(i)))
            vowelCount[j] += 1
        else:
            vowelCount[j] = 1
print(vowelCount)
    
l1 = "Hello World" #ENUMERATE FUNCTION OF LIST, TUPLE, DICTIONARY
for ele in enumerate(l1):
    print (ele)
for count, ele in enumerate(l1):
    print("{} is at index {}".format(ele, count))