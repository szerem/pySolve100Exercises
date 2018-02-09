def acceleration(v1, v2, t1, t2):
    v1, v2, t1, t2 = 1.0*v1, 1.0*v2, 1.0*t1, 1.0*t2 
    return (v2-v1)/(t2-t1)
    
print(acceleration(0, 10, 0, 20))
