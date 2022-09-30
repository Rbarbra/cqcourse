S1 = {"Hello","World","How","Are","You"}
print(type(S1))
print(S1)

S2 = set(range(10))
print(type(S2))
print(S2)

Ls1 = [5,6,7,8,5,1,2,5,9,4,6]
print(Ls1)
S3 = set(Ls1)
print(type(S3))
print(S3)

Ls2 = list(S3)
print(type(Ls2))
print(Ls2)

print(S2)
elem1 = S2.pop()
print(S2)
elem2 = S2.pop()
print(S2)
S2.add(elem1)
print(S2)
S2.add(elem2)
print(S2)
S2.pop()
print(S2)