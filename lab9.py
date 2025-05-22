import math

def g(x):
    return math.sqrt(4 - math.log(x))

def simple_iteration_method(a, b, epsilon):
    x_n = a
    
    while True:
        x_next = g(x_n)  
        if abs(x_next - x_n) < epsilon:  
            return x_next  
        x_n = x_next  

a = 1.0  
b = 2.0  
epsilon = 1e-6  

root = simple_iteration_method(a, b, epsilon)
print(f"Tənliyin təqribi kökü: {root}")
