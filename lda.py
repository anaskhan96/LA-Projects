import numpy as np
from functools import reduce

feature1 = [0.5, 1, 1, 1.5, 1.5, 2, 3, 3.5, 3.5, 4, 4.5]
feature2 = [1.5, 1.5, 2, 2, 2.5, 2.5, 1, 1, 2, 2, 2]
classType = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1])


def find_pivot(f1, f2):
    f1 = np.array(f1)
    f2 = np.array(f2)
    pivot_arr = calculate_pivot(f1,f2)
    end_pivot = reduce(lambda x,y: (x-y)/2, pivot_arr)
    return end_pivot


def calculate_pivot(f1,f2):
    return (f1-f2)/2

x = float(raw_input('Enter the value of feature 1 :'))
y = float(raw_input('Enter the value of feature 2 :'))
pivot = find_pivot(feature1, feature2)
point = calculate_pivot(x,y)
if point < pivot:
    print 'Class 0'
else:
    print 'Class 1'