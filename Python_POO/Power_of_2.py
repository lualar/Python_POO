def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

#Interactor
for v in powers_of_2(8):
    print(v)

print()
#List Comprehensions
t = [x for x in powers_of_2(8)]
print(t)

print()
#List Return
t = list(powers_of_2(3))
print(t)

print()
#In operator
for i in range(20):
    if i in powers_of_2(8):
        print(i)