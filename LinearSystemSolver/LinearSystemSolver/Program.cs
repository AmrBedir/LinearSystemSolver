using System;

class LinearSystemSolver
{
    static void Main(string[] args)
    {
        Console.WriteLine("Linear System Solver - Task Assignment");
        Console.WriteLine("Second Level - First Semester: 2023-2024\n");
        Console.WriteLine("Name: Amr Bedir Taher");
        Console.WriteLine("ID: 1000264365");
        Console.WriteLine("Group: 2, Section: 12");
        Console.WriteLine("\n____________________\n");

        Console.Write("Enter the number of equations: ");
        int n = int.Parse(Console.ReadLine());

        // Create a matrix to store the coefficients and constants of the linear system
        double[,] matrix = new double[n, n + 1];

        // Input coefficients and constants for each equation
        for (int i = 0; i < n; i++)
        {
            Console.WriteLine($"Enter coefficients for equation {i + 1}:");
            for (int j = 0; j < n; j++)
            {
                Console.Write($"a{i + 1}{j + 1}: ");
                matrix[i, j] = double.Parse(Console.ReadLine());
            }

            Console.Write($"Enter the constant (b{i + 1}): ");
            matrix[i, n] = double.Parse(Console.ReadLine());
        }

        // Perform Gaussian elimination to convert the matrix into upper triangular form
        for (int k = 0; k < n; k++)
        {
            for (int i = k + 1; i < n; i++)
            {
                double factor = matrix[i, k] / matrix[k, k];
                for (int j = k; j <= n; j++)
                {
                    matrix[i, j] -= factor * matrix[k, j];
                }
            }
        }

        // Backward substitution to find the solution
        double[] solution = new double[n];
        for (int i = n - 1; i >= 0; i--)
        {
            solution[i] = matrix[i, n];
            for (int j = i + 1; j < n; j++)
            {
                solution[i] -= matrix[i, j] * solution[j];
            }
            solution[i] /= matrix[i, i];
        }

        // Display the solution with steps
        Console.WriteLine("\n____________________\n");
        Console.WriteLine("Solution with Steps:");
        for (int i = 0; i < n; i++)
        {
            Console.Write($"x{i + 1} = ({matrix[i, n] / matrix[i, i]:0.00})");

            for (int j = 0; j < n; j++)
            {
                if (j != i)
                {
                    Console.Write($" - ({matrix[i, j]:0.00} * x{j + 1})");
                }
            }

            Console.WriteLine();
        }

        // Display the final solution
        Console.WriteLine("\n____________________\n");
        Console.WriteLine("Final Solution:");
        for (int i = 0; i < n; i++)
        {
            Console.WriteLine($"x{i + 1} = {solution[i]:0.00}");
        }
    }
}