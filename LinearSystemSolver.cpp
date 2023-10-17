#include <iostream>
#include <vector>

using namespace std;

int main() {
    cout << "Linear System Solver - Task Assignment" << endl;
    cout << "Second Level - First Semester: 2023-2024" << endl;
    cout << "\nName: Amr Bedir Taher" << endl;
    cout << "ID: 1000264365" << endl;
    cout << "Group: 2, Section: 12" << endl;
    cout << "\n____________________\n" << endl;

    cout << "Enter the number of equations: ";
    int n;
    cin >> n;

    // Create a matrix to store the coefficients and constants of the linear system
    vector<vector<double>> matrix(n, vector<double>(n + 1));

    // Input coefficients and constants for each equation
    for (int i = 0; i < n; i++) {
        cout << "Enter coefficients for equation " << i + 1 << ":" << endl;
        for (int j = 0; j < n; j++) {
            cout << "a" << i + 1 << j + 1 << ": ";
            cin >> matrix[i][j];
        }

        cout << "Enter the constant (b" << i + 1 << "): ";
        cin >> matrix[i][n];
    }

    // Perform Gaussian elimination to convert the matrix into upper triangular form
    for (int k = 0; k < n; k++) {
        for (int i = k + 1; i < n; i++) {
            double factor = matrix[i][k] / matrix[k][k];
            for (int j = k; j <= n; j++) {
                matrix[i][j] -= factor * matrix[k][j];
            }
        }
    }

    // Backward substitution to find the solution
    vector<double> solution(n);
    for (int i = n - 1; i >= 0; i--) {
        solution[i] = matrix[i][n];
        for (int j = i + 1; j < n; j++) {
            solution[i] -= matrix[i][j] * solution[j];
        }
        solution[i] /= matrix[i][i];
    }

    // Display the solution with steps
    cout << "\n____________________\n" << endl;
    cout << "Solution with Steps:" << endl;
    for (int i = 0; i < n; i++) {
        cout << "x" << i + 1 << " = (" << matrix[i][n] / matrix[i][i] << ")";
        for (int j = 0; j < n; j++) {
            if (j != i) {
                cout << " - (" << matrix[i][j] << " * x" << j + 1 << ")";
            }
        }
        cout << endl;
    }

    // Display the final solution
    cout << "\n____________________\n" << endl;
    cout << "Final Solution:" << endl;
    for (int i = 0; i < n; i++) {
        cout << "x" << i + 1 << " = " << solution[i] << endl;
    }

    return 0;
}
