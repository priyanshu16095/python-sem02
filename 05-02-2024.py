# TUPLES : IMMUTABLE

t1 = (1, 'raju', 28, 'abc')
type(t1)

t2 = ('satish',) #t2 = "satish",

t3 = ('ABC', ('car', 'bike', 'truck'))
print(t3[1])
print(t3[1][1]) #BIKE
print(t3[:]) #PRINT ALL ELEMENTS
print(t3[:-4]) #FROM LAST TILL -4 

t4 = t2 + t3

t5 = (('satish',) * 4)
del t5 

t6 = (1, 5, 1, 2, 3)
t6.count(1)
print(1 not in t6) #MEMBERSHIP
print(max(t6))
print(min(t6))

t7 = ('c', 'a', 'c', 'd', 'e')
t7.count('c')

t8 = (2 , 3, 5, 7, 9, 8, 4, 3)
sum = 0
for i in t8:
    if(i == 9):
        break 
    else:
        sum += i
print(sum)