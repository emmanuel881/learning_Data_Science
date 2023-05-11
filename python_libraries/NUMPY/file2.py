import numpy as np
#..... create a matrix of zeros .......#
print(np.zeros((2, 3)), "\n")
#it takes shape of the matrix as an argument

#..... create a matrix of ones .......#
print(np.ones((2,2)), "\n")

#.......of different values ........#
print(np.full((2, 2), 33),"\n")

#...................pass random variables ..............#
rand_matrx = np.random.rand(2, 2)
print(rand_matrx, "\n")

#............... random integers ......#
rand_int = np.random.randint(11, size= (2, 2))
print(rand_int)