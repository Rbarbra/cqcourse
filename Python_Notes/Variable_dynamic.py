for n in range(0, 7):
    globals()['strg%s' % n] = 'Hello'

print(strg5)

for x in range(0, 7):
    globals()[f"variable1{x}"] = f"Hello the variable number {x}!"

print(variable15)