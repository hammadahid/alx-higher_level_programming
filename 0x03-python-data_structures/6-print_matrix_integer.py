#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    m = ""
    if matrix is None:
        return 0
    for i  in matrix:
        for a in range(0, len(i)):
            if a < len(i) -1:
                print("{:d} ".format(i[a]), end ="")
            else:
                print("{:d}".format(i[a]), end ="")
        print()
