import numpy as np

def matrix_multiply(A, B):
    try:
        A = np.array(A)
        B = np.array(B)
        if A.shape[1] != B.shape[0]:
            raise ValueError("Error: Matrices are not multiplicable")
        result = np.dot(A, B)
        print("Product AB:")
        print(result)
    except Exception as e:
        print(e)
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
matrix_multiply(A, B)
