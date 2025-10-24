import math

print("Hello World")
x = True
print(x)
print(type(x))

def inspect(x):
    if x == 0:
        print(x,"is zero")
    elif x < 0:
        print(x,"is negative")
    elif x > 0:
        print(x,"is positive")
    else:
        print("Unlikely to be seen such thing")
inspect(19)

primes = [2,4,3,5,7]
hello = [
    [1,2,3],
    [2,4,6]
]

lst = [1,"Hello World",3]

x = 12
print(x.imag)

c = 12 + 3j
print(c.imag)

#tuples
tup =(1,2,3)

#List Comprehensions
list=[n**2 for n in range(10)]
print(list)

print("My dog's name is Pluto")
print('Pluto \'s a planet')

print("hello\nworld")
planet = "Pluto"
position = 9
print("{},is at the,{}th position".format(planet,position))

#dictionary
numbers ={'one':1, 'two':2, 'three':3}
print(numbers)

print(numbers['one'])
numbers['eleven'] = 11
print(numbers)

for k in numbers:
    print("{} = {}".format(k,numbers[k]))

print(dir(math))
print("pi to 4 significant bits{:.4}".format(math.pi))
print(math.log(32,5)) #log of x to the base m (math.log(x,m))

planets=['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']
for planet in planets:
    print(planet,end=' ')