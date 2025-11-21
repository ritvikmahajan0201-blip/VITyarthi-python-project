#matrice multiplier program 
import numpy as np
valuesA = []
valuesB = []
order_matrixA = input("Pls tell the order of the matrix(m x n): ")
print("Enter values for matrix A")
for i in range(1,(int(order_matrixA[0])*int(order_matrixA[2]))+1):
    value = int(input(f"Enter {i} value: "))
    valuesA.append(value)
array1 = np.array(valuesA).reshape(int(order_matrixA[0]),int(order_matrixA[2]))

print("Enter values for matrix B")
for i in range(1,(int(order_matrixA[0])*int(order_matrixA[2]))+1):
    value = int(input(f"Enter {i} value: "))
    valuesB.append(value)
array2 = np.array(valuesB).reshape(int(order_matrixA[2]),int(order_matrixA[0]))

print(f"result:{array1.dot(array2)}")