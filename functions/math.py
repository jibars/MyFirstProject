def create_matrix(number_of_rows, number_of_columns):
    return [[None] * number_of_columns for i in range(number_of_rows)]

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

def identity(size):
    identity_array = [[0.0] * size for i in range(size)]
    for row in range(size):
        identity_array[row][row] = 1.0
    return identity_array

def create_extended_array(array):
    size = len(array)
    identity_array = identity(size)
    return [array[i] + identity_array[i] for i in range(size)]

def inverse(array):
    number_of_rows = len(array)
    extended_array = create_extended_array(array)
    for row in range(number_of_rows):
        pivot = extended_array[row][row]
        number_of_columns = len(extended_array[row])
        for column in range(number_of_columns):
            extended_array[row][column] = extended_array[row][column] / pivot
        i = 0
        for i in range(number_of_rows):
            if i != row:
                pivot = extended_array[i][row]
                for j in range(number_of_columns):
                    extended_array[i][j] = extended_array[i][j] - pivot * extended_array[row][j]
    return extended_array
