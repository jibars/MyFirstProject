def create_matrix(number_of_rows, number_of_columns):
    return [[None] * number_of_columns for i in range(number_of_rows)]

def create_extended_array(array):
    number_of_rows = len(array)
    number_of_columns = len(array)
    identity_array = [[0.0] * number_of_rows for i in range(number_of_columns)]
    for row in range(number_of_rows):
        for column in range(number_of_columns):
            if column == row:
                identity_array[row][column] = 1.0

def determinant(array):
    number_of_rows = len(array)
    column = 0
    if number_of_rows == 1:
        return array[0][column]
    sum = 0
    for row in range(number_of_rows):
        number_of_columns = len(array[row])
        if number_of_rows != number_of_columns:
            raise Exception
        sum += (-1) ** (row + column) * array[row][column] * determinant([[array[i][j] for j in range(number_of_columns) if j != column] for i in range(number_of_rows) if i != row])
    return sum



#def inverse(array):
#    number_of_rows = len(array)
#    extended_array = create_extended_array(array)
#    for row in range(number_of_rows):
#        number_of_columns = len(array[row])
#        if number_of_rows != number_of_columns:
#            raise Exception
#        for columns in range(number_of_columns):

