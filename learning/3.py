import math
def square(a):
    p = a*4
    s = a ** 2
    c = (math.sqrt(2 * s))
    return tuple((p, s, c))
a = int(input("vvedite chislo "))
print("perimetr/ploshad/diagonal ", square(a))