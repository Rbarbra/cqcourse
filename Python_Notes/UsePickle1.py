import pickle,random
RanNR1 = random.randint(0,100)
RanNR2 = random.random()
RanNR3 = random.gauss(1,5)
RanLS1 = list(range(random.randint(0,100)))
random.shuffle(RanLS1)

print(RanNR1)
print(RanNR2)
print(RanNR3)
print(RanLS1)

pickle.dump((RanNR1,RanNR2,RanNR3,RanLS1),open("Example.pickle","wb"))
