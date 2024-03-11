dict1 = {'mango': 5, 'apple': 2, 'banana': 8, 'grapes': 1}
dict2 = dict(dict1)
dict3 = dict1.copy()

dict1['mango']
dict1['mango'] = 6
dict1['watermelon'] = 3

max(dict1,  key=dict1.get)
min(dict1,  key=dict1.get)
len(dict1)

if 'mango' in dict1:
    print("Present")
    
dict1.keys()    # Returns a list 
dict1.values()  # Returns a list
dict1.items()   # Returns a list of tuples

dict1.clear()
del dict1