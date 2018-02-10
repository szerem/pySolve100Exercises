from math import pi

def liquid (h, r=10):
    l = float((4 * pi * r**3) / 3) -float( (pi * h**2 * (3*r-h)) / 3)  
    return l

print(liquid(2))