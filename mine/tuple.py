tuple1 = (7, 8, 1, 2, 3)
tuple2 = (11, 15)

list1 = tuple1 + tuple2
tuple3 = tuple1 + tuple2
tuple4 = tuple1 * 2     # (7, 8, 1, 2, 3, 7, 8, 1, 2, 3)

tuple1[0]
tuple1[0:4]
tuple1.count(8)
tuple1.index(8)
max(tuple1)
min(tuple1)
len(tuple1)

if 2 in tuple1:
    print("Present")
    
a, b = tuple2