print("Surprise test")

l1 = ['one', 'two', 'three']
l2 = [[1, 2], [3, 4]]
l3 = list(range(1, 11))

l4 = []
even = []
odd = []
n = int(input("Enter the number of elements: "))
for i in range(0, n):
    ele = int(input("Enter the element: "))
    if(ele % 2 == 0):
        print("Even no is {}".format(ele))
        even.append(ele)
    else:
        print("Odd no is {}".format(ele))
        odd.append(ele)
    l4.append(ele)
print(even)
print(odd)
