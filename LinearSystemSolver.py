def main():
    print("Linear System Solver - Task Assignment")
    print("Second Level - First Semester: 2023-2024\n")
    print("Name: Amr Bedir Taher")
    print("ID: 1000264365")
    print("Group: 2, Section: 12")
    print("\n____________________\n")

    n = int(input("Enter the number of equations: "))

    # Create a matrix to store the coefficients and constants of the linear system
    matrix = [[0] * (n + 1) for _ in range(n)]

    # Input coefficients and constants for each equation
    for i in range(n):
        print(f"Enter coefficients for equation {i + 1}:")
        for j in range(n):
            matrix[i][j] = float(input(f"a{i + 1}{j + 1}: "))

        matrix[i][n] = float(input(f"Enter the constant (b{i + 1}): "))

    # Perform Gaussian elimination to convert the matrix into upper triangular form
    for k in range(n):
        for i in range(k + 1, n):
            factor = matrix[i][k] / matrix[k][k]
            for j in range(k, n + 1):
                matrix[i][j] -= factor * matrix[k][j]

    # Backward substitution to find the solution
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = matrix[i][n]
        for j in range(i + 1, n):
            solution[i] -= matrix[i][j] * solution[j]
        solution[i] /= matrix[i][i]

    # Display the solution with steps
    print("\n____________________\n")
    print("Solution with Steps:")
    for i in range(n):
        print(f"x{i + 1} = ({matrix[i][n] / matrix[i][i]:0.2f})", end="")
        for j in range(n):
            if j != i:
                print(f" - ({matrix[i][j]:0.2f} * x{j + 1})", end="")
        print()

    # Display the final solution
    print("\n____________________\n")
    print("Final Solution:")
    for i in range(n):
        print(f"x{i + 1} = {solution[i]:0.2f}")


if __name__ == "__main__":
    main()
