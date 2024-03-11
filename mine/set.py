# collection of unique elements, unordered, iterable, mutable

set1 = {7, 8, 1, 2, 3}
set2 = set(set1)
set3 = set([7, 8, 1, 2, 3])
set4 = set.copy(set1)

set1.add(11)
set1.update([15, 6, 19])
set1.remove(15)     # raise error if not present
set1.discard(15)    # does nothing if not present
set1.pop()

union = set1.union(set2)
inters = set1.intersection(set2)
diff = set1.difference(set2)
symDiff = set1.symmetric_difference(set2)

set1.clear()
del set1