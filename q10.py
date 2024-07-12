import numpy as np


def function_to_return_transpose(matrix):
    numpy_matrix = np.array(matrix)
    return numpy_matrix.transpose()


def display_matrix(matrix):
    for row in matrix:
        print(row)


# driver code..
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("my matrix...")
display_matrix(my_matrix)
print("Transpose of my matrix")
tranpose_of_my_matrix = function_to_return_transpose(my_matrix)
display_matrix(tranpose_of_my_matrix)
