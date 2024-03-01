dict1 = {}
dict1 = {"apple": 1, "banana": 2, "mango": 5}

if "apple" in dict1:
    print("Present")

dict1["watermelon"] = 11 #adding a new key pair

# dict1.update(dict2)

dict1.pop("apple") #remove and return the value associated with key
dict1.popitem()

del dict1
dict1.clear()

dict1.keys()
dict1.values()
dict1.items()

dict2 = dict1.copy()
dict2 = dict(dict1)

len(dict1)