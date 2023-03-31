import numpy as np

#Pegamos uma lista em python e transformamos em vetor
numbers = np.array([-5, 4, 0, 2, 3])
positives = numbers[numbers > 0]
print(positives)
# array([4, 2, 3])


numbers = np.array([-5, 4, 0, 2, 3])
is_positive = numbers > 0
print(is_positive)

matrix = np.array([[1, 2, 3], 
[4, 5, 6], 
[7, 8, 9]])

print(np.array([[1, 2, 3], 
[4, 5, 6], 
[7, 8, 9]])) 