t1 = (1, 2, 3, 4, 5)
print(len(t1))

t2 = (7, 8, 1, 2, 3)
t3 = sorted(t2) #DOES NOT SORT THE TUPLE, ONLY THE OUTPUT   
print(t3)

print(sum(t3))
print(min(t3))
print(max(t3))
    
t4 = ('Priyanshu', 'Nobita', 'Abhay')
t5 = ('Gupta', 'Nobi', 'Ambani')
t7 = (18, 15, 19)
for i in range(len(t4)):
    if(t7[i] >= 18):
        print("{}, {}, {}".format(t4[i]+' '+t5[i], t7[i], "Eligible"))
    else:
        print("{}, {}, {}".format(t4[i]+' '+t5[i], t7[i], "Not Eligible"))

firstName = []
lastName = []
age = []
eligiblity = []
while True:
    fname = input("Enter the first name: ")
    lname = input("Enter the last name: ")
    umar = int(input("Enter the age: "))
    if(umar >= 18):
        eligiblity.append('Eligible')
    elif(age < 0):
        print("Not a valid age")
    else:
        eligiblity.append('Not Eligible')
    firstName.append(fname)
    lastName.append(lname)
    age.append(umar)

    res = input("Do you want to continue? (y/n): ")
    if(res.lower() != 'y'):
        break
print('Name | Age | Eligible')
for i in range(len(firstName)):
    print("{} {} {} {}".format(firstName[i], lastName[i], age[i], eligiblity[i]))