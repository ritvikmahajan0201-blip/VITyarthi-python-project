vect_A = [3, -5, 4]
vect_B = [2, 6, 5]
cross_P = [ ]
cross_P.append(vect_A[1] * vect_B[2] - vect_A[2] * vect_B[1])
cross_P.append(vect_A[2] * vect_B[0] - vect_A[0] * vect_B[2])
cross_P.append(vect_A[0] * vect_B[1] - vect_A[1] * vect_B[0])
print("Cross product:", end =" ")
for i in range(0, 3):
    print(cross_P[i], end =" ")