multiply_lambda = lambda elements, multiplier=2: [element * multiplier for element in elements]

print(multiply_lambda([1, 2, 3])) # [2, 4, 6]
print(multiply_lambda([1, 2, 3], 3)) # [3, 6, 9]
