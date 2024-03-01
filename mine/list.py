list1 = [] 
list1 = [1, 2, 3]

list1.append(7)

nums = [4, 5, 6]
list1.extend(nums)

# append is used to add a single element 
# extend is used to add an iterable
# both add to the end of the list

list1[2]   #index
list1[1:5]

if 2 in list1:
    print("Present")
else:
    print("Not present")

list1.remove(2) #list.remove(element)
# remove will remove the first occurence of that element

list1.pop() # remove and return the last element

list1.clear()
del list1

list1.index(2) #list.index(element)
list1.count(2) #list.count(element)
list1.reverse()
list1.sort()
list1.sort(reverse=True)

anotherList = list1.copy()
anotherList = list(list1)

len(list1) 
max(list1) #maximum element in the list
min(list1) #minimum element is the list

