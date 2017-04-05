import numpy as np

# Given input data
interval = [1, 2]
polynomial = [1, 4, 0, -10] # x**3 + 4*x**2 - 10

p = np.poly1d(polynomial)
q = p.deriv() # derivative of the polynomial
count = 0 # counting the iterations

def g(x):
    global count
    result = x - (p(x)/float(q(x)))
    diff = abs(result - x)
    count += 1
    if diff < 0.001: # taking 10^-3 as tolerance limit
        print result
    else:
        g(result)

g(interval[0]) # calling the function to start the iteration
print count