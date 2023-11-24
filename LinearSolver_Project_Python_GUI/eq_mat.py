import re
import numpy

def equationToMatrix(numberOfVariables,eq):
    rows,cols = (numberOfVariables,numberOfVariables+1)
    A = numpy.empty(shape=(numberOfVariables,numberOfVariables+1))
    for i in range(0,numberOfVariables):
        coefs =re.findall(r'[0-9\-\+]+', eq[i])
        #print(coefs)
        for j in range(0,numberOfVariables+1):
            if coefs[j] == "+" or coefs[j] == "-":
                coefs[j] = coefs[j]+"1"
            elif len(coefs)<numberOfVariables+1:
                coefs.insert(0,"1")
            A[i][j] = float(coefs[j])
            #print(A[i][j])
    return A

def inputToMatrix(numberOfVariables, equations):
    matrix = numpy.zeros((numberOfVariables, numberOfVariables + 1))
    eqnNum = 0
    equations = equations.split(',')

    count = 0
    for _ in equations:
        equations[count] = '+' + equations[count]
        count += 1

    for i in equations:
        eqnCoef = re.findall(r'[(\d+|\d+\.\d+)\-\+]+', i)

        coef = 0
        for j in eqnCoef:
            if j == '-':
                eqnCoef[coef] = '-1'
            elif j == '+':
                eqnCoef[coef] = '1'
            elif j == '+-':
                eqnCoef[coef] = '-1'
            elif len(j) > 2 and j.startswith('+-'):
                eqnCoef[coef] = j[1:]
            if coef == numberOfVariables:
                matrix[eqnNum][coef] = float(eqnCoef[coef]) * 1.0
            else:
                matrix[eqnNum][coef] = float(eqnCoef[coef])
            coef += 1
        eqnNum += 1
    return matrix
