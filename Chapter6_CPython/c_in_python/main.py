import math_cpython


l1 = [i for i in range(10)]
l2 = [i for i in range(10)]
result = math_cpython.add(l1, l2)
print(result)

min_value = 2
max_value = 4
l3 = [i for i in range(10)]

math_cpython.clip(l3, min_value, max_value)
print(l3)
