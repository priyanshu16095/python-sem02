a = 2; b =3; c = 4
p = q = r = 10

# PYTHON USES UNICODE

print(id(a)) # ADDRESS

# SAME ADDRESS
i = 3
j = 3
print(id(i))
print(id(j))

# DIFFERENT ADDRESS
k = 3
p = 30
print(id(k))
print(id(p))

m = 5 + 6J
print(isinstance(m, complex))

