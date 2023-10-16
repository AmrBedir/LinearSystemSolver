# Algebra - Linear System Solver


### What is required in the task?

* **Program Input:** 
  * Number of equations.
  * Coefficients for every equation.
  
* **Program Output:** 
  * Solution with steps.
  * Final system solution.


### Task code in C#

```c#
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
```
[*Code File*](https://github.com/AmrBedir/LinearSystemSolver/blob/main/LinearSystemSolver/LinearSystemSolver/Program.cs)

### Important to know
**A linear system of equations is a mathematical representation of multiple linear equations with multiple variables that are interconnected. These systems are used to model and solve a wide range of real-world problems across various fields, including physics, engineering, economics, and more. Here's an explanation of key concepts related to linear systems:**

**Linear Equation**: *A linear equation is a mathematical equation in which each term is either a constant or the product of a constant and a single variable raised to the power of 1 (i.e., a linear term). Linear equations can be written in the form ax + by = c, where a, b, and c are constants, and x and y are variables.*

**Linear System of Equations**: *A linear system consists of multiple linear equations. For example, a 2D linear system involves two linear equations with two variables, and a 3D linear system involves three linear equations with three variables.*

**Variables**: *Variables are the unknown quantities you aim to solve for in the linear system. Commonly used variables are x, y, z, and so on. The goal is to find values for these variables that simultaneously satisfy all equations in the system.*

**Coefficients**: *Coefficients are the constants that multiply the variables in each equation. They determine the relative importance of each variable in the equation. For example, in the equation 2x + 3y = 10, 2 and 3 are coefficients.*

**Constants**: *Constants are the terms that do not involve variables. In the equation, 2x + 3y = 10, 10 is the constant term.*

**Solution**: *A solution to a linear system is a set of values for the variables that satisfy all the equations simultaneously. This means that when you substitute these values into each equation, the equations are true.*

**Underdetermined System**: *An underdetermined system has fewer equations than variables. These systems may have infinitely many solutions or no solution at all, depending on the specific equations.*

**Overdetermined System**: *An overdetermined system has more equations than variables. These systems often have no exact solution, but you can find the "best fit" solution that minimizes the error.*

**Gaussian Elimination**: *Gaussian elimination is a method for solving linear systems. It involves a sequence of operations on the equations to transform the system into an upper triangular form, making it easier to solve.*

**Matrix Representation**: *Linear systems are often represented using matrices. The coefficient matrix contains the coefficients of the variables, and the constant matrix contains the constants from each equation. By performing matrix operations, you can solve the system.*

**Unique Solution**: *A linear system has a unique solution when there is exactly one set of values for the variables that satisfy all equations. This occurs when the system is square (the number of equations equals the number of variables) and the determinant of the coefficient matrix is nonzero.*

**No Solution**: *A linear system has no solution when there are conflicting equations, and it's impossible to find values for the variables that satisfy all of them.*

**Infinite Solutions**: *A linear system has infinitely many solutions when it contains redundant equations, and these equations do not provide new information. In such cases, the system can be underdetermined, and any values that satisfy the non-redundant equations are valid solutions.*

**Linear systems are fundamental in mathematics and play a crucial role in scientific and engineering applications. They provide a structured way to model and analyze relationships between multiple variables and are solved using various methods, including Gaussian elimination, matrix algebra, and numerical techniques.**

### Reference explains linear algebra
* [Linear Algebra - Dr. Mervat Mikhail](https://www.youtube.com/playlist?list=PL7snZ0LSsq3gIc4bYM-OnvLZt2KpFvd2_)
