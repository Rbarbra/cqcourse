import random

RanNR1 = random.randint(0,100)
RanNR2 = random.random()
RanNR3 = random.gauss(1,5)

print(RanNR1)
print(RanNR2)
print(RanNR3)

RanLS1 = list(range(random.randint(0,100)))
print(RanLS1)
random.shuffle(RanLS1)
print(RanLS1)