# SET
# Collection of unordered elements
# Do not allow deuplicate values and is immutable and unindexed
# The order in which values are stroed is not preserved

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union of sets
union_set = set1 | set2  # or use set1.union(set2)

# Intersection of sets
intersection_set = set1 & set2  # or use set1.intersection(set2)

# Difference of sets
difference_set = set1 - set2  # or use set1.difference(set2)

x = set1.pop() # Remove any random element\

set1.clear() # Empty the set

# To join two sets use union and update function

x = {"apple", "banana", "grapes"}
y = {"mango", "watermelon", "orange"}
x.intersection_update(y)

set3 = frozenset([1, 2, 3, 4])

# remove will show error if the element is not present
# discard will not show any error if the element is not present

s = [1, 2, 3, {2, 3}, 10, 12]
sum = 0
for i in s:
    if(type(i) == set):
        break
    else:
        sum += i
print(sum)

count = 0
s = [1 , 2, (2, 5), (6, 7, 8), 6, 2]
for i in s:
    if(type(i) == tuple):
        for j in i:
            count += j
print(count)
