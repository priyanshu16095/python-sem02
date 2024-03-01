l1 = [1, 2, 3, 8]
l1.insert(2, "Hello")
print(l1)

# append, extend, insert, pop, reverse

l2 = ['one', 'two', 'three']
if 'two' in l2:
    print("Present")
else:
    print("Not Present")

l3 = [7, 8, 1, 2, 3]
rev_l3 = sorted(l3)
print(rev_l3)

s = "hello how # are you"
a = s.split('#')
print(a)

l4 = ['car', 'truck', 'bike']
l5 = [7, 8, 1, 2, 3]
l6 = l4 + l5
print(l6)
print(l6.count('car'))

s = '1111010'
if s.count('0') or s.count('1')==1:
    print('Yes')
else:
    print('No')

lst = [12, 23, 23, 56, 67, ]