foo = (1, 2, 3)
bar = (4, 5, 6)
tri = (7, 8, 9, 10)

for f, b in zip(foo, bar):
    print(f, b)

newlist = [(elem1, elem2) for (elem1, elem2) in zip(foo, bar)]
print(newlist)

for f, b, t in zip(foo, bar, tri):
    print(f, b, t)