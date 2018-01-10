import functions.math as math



def ask_for_size():
    rows = int(input("Number of rows: "))
    columns = int(input("Number of columns: "))
    return rows, columns

def fill_array(array):
    number_of_rows = len(array)
    for i in range(number_of_rows):
        number_of_columns = len(array[i])
        for j in range(number_of_columns):
            array[i][j] = float(input("A[{0}][{1}]=".format(i, j)))


rows, columns = ask_for_size()
array = math.create_matrix(rows, columns)
fill_array(array)
print(array)
value = math.determinant(array)
print(value)
#try:
#    inverse = math.inverse(array)
#except math.InverseMatrixError, ex:
#    print(ex)
#else:
#    show.print_array(inverse)
#    product = math.matrix_product(array, inverse)
#    show.print_array(product)
