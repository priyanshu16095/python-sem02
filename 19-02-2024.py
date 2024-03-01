dict1 = {"apple": 1, "banana": 5, "watermelon": 2}

# {"apple": 1} was overriden by {"apple": 3}
# dict1 = {"apple": 1, "apple": 3, "banana": 5, "watermelon": 2} 

x = dict1.get("apple")

dict1Keys = dict1.keys()
dict1Values = dict1.values()

dict1["mango"] = 6   #Adding new key
dict1["apple"] = 3   #Updating existing key
dict1.update({"apple": 4})

dict1.pop("apple")
del dict1["banana"]
# del dict1   #Delete whole dictionary
dict1.clear()

dict2 = {"car": 3, "bike": 5, "truck": 1}
for i in dict2:
    print(i)
    print(dict2[i])
for item, count in dict2.items():
    print("{} : {}", item, count)

#Only method to copy a dictionary
dict3 = dict2.copy()
#Or
dict4 = dict(dict3)