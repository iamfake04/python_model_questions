def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    
    return transposed

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Example usage
if __name__ == "__main__":
    matrix1 = [
        [1, 2, 1],
        [4, 5, 1],
        [7, 8, 1]
    ]
    
    matrix2 = [
        [9, 8, 1],
        [6, 5, 1],
        [3, 2, 1]
    ]
    
    # Add the matrices
    result_matrix = add_matrices(matrix1, matrix2)
    print("Resultant Matrix (Addition):")
    print_matrix(result_matrix)
    
    # Transpose the resultant matrix
    transposed_matrix = transpose_matrix(result_matrix)
    print("\nTransposed Matrix:")
    print_matrix(transposed_matrix)