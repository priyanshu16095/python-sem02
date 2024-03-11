denominations = [2000, 500, 200, 100, 50, 20, 10]
amount = 3000
noteCount = {}
for denomination in denominations:
    count = amount // denomination
    if count > 0:
        noteCount[denomination] = count
        amount %= denomination
print(noteCount)

text = """
    Honorable Prime Minister's Independence Day speech goes here.
    This is just a sample text for demonstration purposes.
"""
words = text.lower().split()
wordCount = {}
for word in words:
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1
        
items = ['pen', 'ball', 'eraser', 'pen', 'band', 'pen', 'pencil', 'ball']
itemCount = {}
for item in items:
    if item in itemCount:
        itemCount[item] += 1
    else:
        itemCount[item] = 1
print(itemCount)
        
tuple1 = (7, 8, 1, 2, 3)
list1 = list(tuple1)
list1.append(11)
list1.remove(8)
tuple1 = tuple(list1)
print(tuple1)

set1 = {'a', 'b', 'e', 'i', 'o', 'u', 'a', 'b', 'c', 'e', 'i', 'o', 'u'}
vowels = {'a', 'e', 'i', 'o', 'u'}
charCount= {}
for char in set1:
    if char in vowels:
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1
print(charCount)
        
        
        
        
        
        
        
        
        
        