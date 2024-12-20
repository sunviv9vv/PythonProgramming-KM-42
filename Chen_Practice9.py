import numpy as np
import itertools

def random_matrix(dim):
    """
    The function generates dim x dim array of integers
    between 0 and 10.
    """
    matrix = np.random.randint(10, size = (dim, dim))
    return matrix

def create_permutations_list(dim):
    """
    Create all permutations of a list of length dim.
    """
    t = list(itertools.permutations(range(dim)))
    return t


def calculate_product(matrix, permutation):
    """
    Calculate the product of matrix elements corresponding to the given permutation.
    """
    product = 1

    for i in range(len(permutation)):
        product *= matrix[i][permutation[i]]
    return product

def calculate_determinant(matrix):
    """
    Calculate the determinant of a matrix using the rule of permutations.
    """
    dim = len(matrix)
    permutations = create_permutations_list(dim)
    determinant = 0

    for p in permutations:
        inversions = sum (1 for i in range(len(p)) for j in range(i + 1, len(p)) if p[i] > p[j])
        sign = (-1) ** inversions
        determinant += sign * calculate_product(matrix, p)
    return determinant

def main():
    try:
        dim = int(input("Enter the dimension of the matrix (positive integer): "))
        if dim <= 0:
            print("Please enter a positive integer.")
            return
        
        matrix = random_matrix(dim)
        print("Generated matrix:")
        print(matrix)
        deter = calculate_determinant(matrix)

        print("Determinant calculated using the rule of permutations: ", deter)
        print("Determinant calculated using numpy: ", np.linalg.det(matrix))
        
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
