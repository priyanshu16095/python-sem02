dict1 = {'apple': 1, "banana": 5, "mango": 3}
print(dict1)
print(dict1.get('apple'))
print(dict1['mango'])
print(dict1.keys())
print(dict1.values())

for fruit, count in dict1.items():
    print("There are {} {}".format(count, fruit))

dict1['watermelon'] = 2       #Updating value
dict1['grapes'] = 1           #Adding a new key

dict1.pop('banana')
dict1.popitem()

# dict1.clear() #Dictionary will become empty
# del dict1

dict2 = dict1.copy()

dict3 = {}.fromkeys(['Math', 'English', 'Hindi'], 1)
dict4 = {2:4, 3:9, 4:16, 5:25}

dict5 = {}
print(dir(dict5))

l = [1,1, {1,1,1,1, 1}, (1, 1), 1+4J, {'age': 1}, True, 1.6]
for i in l:
    if(isinstance(i, set)):
        for j in i:
            print(j)
sum = 0
for i in l:
    if(type(i) == bool(True)):
        sum += 1
    if(type(i) == set):
        for j in i:
            sum += j
    if(type(i) == tuple):
        for j in i:
            sum += j
    elif(isinstance(i, dict)):
        for j in i.values():
            sum += j
    elif(isinstance(i, complex)):
        sum += i.real
print("Sum: {}".format(sum))

name = "Priyanshu Gupta"
print(name[::-1])

def reverse_string(input_str):
    reversed_str = ''
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str

# Example
original_str = "Hello, World!"
result = reverse_string(original_str)
print(result)