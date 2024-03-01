tuple1 = ()
tuple1 = (1, 2, 3)

tuple1[1] #index

if 2 in tuple1:
    print("Present")
else:
    print("Not present")

tuple1.index(2) #returns the index
tuple1.count(2)

tuple2 = (4, 5, 6)
newTuple = tuple1 + tuple2 #concatination of tuples
newTuple = tuple1 * 3

a, b, c = tuple1 #unpacking the tuple

len(tuple1)
min(tuple1)
max(tuple1)