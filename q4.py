def transpose_matrix(matrix):
    transposed = list(map(list, zip(*matrix)))
    print("Transposed Matrix:")
    for row in transposed:
        print(row)
matrix = [[1, 2, 3], [4, 5, 6]]
transpose_matrix(matrix)
