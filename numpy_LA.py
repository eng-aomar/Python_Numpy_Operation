from numpy import *
from numpy_operation import *

def input_array_dimensions():
    rows = int(input("Enter number of rows: "))
    columns = int( input("Enter number of Columns: "))
    return rows, columns

def input_array_elements(array_name):
    length = len(array_name)

    for i in range(length):
        for j in range(len(array_name[i])):
            element = int(input(f"Enter Element[{i}][{j}]: "))
            array_name[i][j] = element

    print("#" * 50)
    print("Enterd array: \n", array_name)
    print("#" * 50)
            
avaliable_choices = {
    "1": "Array-2-Array Mathmatics.",
    "2": "Array Manipulation",
    "3": "Exit."
}
math_operationsDict = {
    "+": "Addition.",
    "-": "Subtraction.",
    "/": "Division.",
    "*": "Multiplication.",
    "R": "Return to main menu."
}

array_manipulation_dictionary = {
    
    '1': "Transpose",
    "2": "Reshape",
    "3": "Concatenate vertically",
    "4": "Concatenate horizenalty",
    "5": "Split vertically",
    "6": "Split horizentaly",
    "R": "Return to main menu."
}


def is_number_regex(s):
    """ Returns True is string is a number. """
    if re_match("^\d+?\.\d+?$", s) is None:
        return s.isdigit()
    return True


def print_dictionary(msg, **myDict):
    """ Prints any data of type dictionary
    msg -> any custome msg
    myDict -> any data of type dictionary
     """
    print("=" * 50)
    print(f'{msg}')
    print("=" * 50)
    for key, value in myDict.items():
        print("[{}] {}".format(key, value))
    print("=" * 50)


def handel_input(choice):
    """" Directs the user to the suitable main menu item based """
    if (choice not in avaliable_choices):
        print("Wrong Choice! Please try again.")
        print("-" * 50)
    elif choice == "1":
        print("First Array: ")
        global array_one_rows
        global array_one_columns
        array_one_rows, array_one_columns = input_array_dimensions()
        global array_one      
        array_one = zeros((array_one_rows, array_one_columns), dtype=int)
        input_array_elements(array_one)
        print("-" * 50)
        print("Second Array: ")
        global array_two_rows
        global array_two_columns
        array_two_rows, array_two_columns = input_array_dimensions()
        global array_two
        array_two = zeros((array_two_rows, array_two_columns), dtype=int)
        input_array_elements(array_two)
        msg = " Welcome to our Main Menu:"
        print_dictionary(msg, **math_operationsDict)
        math_operation = input("Please select your operation: ")
        handel_opeartion(math_operation, array_one, array_two)
    elif choice == '2':
        msg = " Welcome to our Main Menu:"
        print_dictionary(msg, **array_manipulation_dictionary)
        operation = input("Please select your operation: ")
        handel_manipulatins_opeartion(operation)


def handel_manipulatins_opeartion(manipulation_operation):

    if manipulation_operation == '1':
        print("First Array: ")
        array_rows, array_olumns = input_array_dimensions()
        array = zeros((array_rows, array_olumns), dtype=int)
        input_array_elements(array)
        print("-" * 50)
        print("Enterd Array: ")
        print(array)
        print("-" * 50)
        print(f"Trasposed Array:")
        result = ArrayManipulation.transposing_array(array)
        print(f"{result}")
    
def handel_opeartion(math_operation, array1, array2):
    """ 
     This function does arethmatic operation.
     math_opeartion -> [+, -, *, /], R for main menu return
     num1= first number
     num2= second number 
     """
    if (math_operation not in math_operationsDict):
        print("-" * 50)
        print("Wrong Choice! Please try again.")
        print("-" * 50)
    elif math_operation == "+":
        if is_equal_dimentions:
            print(f"{array1}")
            print("+")
            print(f"{array2}")
            print(f"=")
            result = ArrayMathmatics.add_matrices(array1, array2)
            print(f"{result}")          
        else:    
            print('Can not add metrices off different dimentions!!')
    elif math_operation == "-":
        if is_equal_dimentions:
            print(f"{array1}")
            print("-")
            print(f"{array2}")
            print(f"=")
            result = ArrayMathmatics.subtract_matrices(array1, array2)
            print(f"{result}")
        else:
            print('Can not subtract metrices off different dimentions!!')
    elif math_operation == "*":
        if is_eligable_for_multiplication:
            print(f"{array1}")
            print("*")
            print(f"{array2}")
            print(f"=")
            result = ArrayMathmatics.multiply_matrices(array1, array2)
        else:
            ('Can not multiple metrices, the number of coulmns for the first must equal to the number of rows for the second array!!')
        print(f"{result}")
    elif math_operation == "/":
        if is_equal_dimentions:

            print(f"{array1}")
            print("/")
            print(f"{array2}")
            print(f"=")
            result = ArrayMathmatics.divide_matrices(array1, array2)
            print(f"{result}")
        else:
            print('Can not add divide metrices off different dimentions!!')
    else:
        print_dictionary("Welcome to the main menu", **avaliable_choices)


def is_equal_dimentions():
  is_equal_dimentions = array_one_rows == array_two_rows and array_one_columns == array_two_columns
  return is_equal_dimentions

def is_eligable_for_multiplication():
    is_columns_of_first_equal_to_rows_of_second = array_one_columns == array_two_rows
    return is_columns_of_first_equal_to_rows_of_second

while True:
    print_dictionary(
        'Welcome to Main Menu', **avaliable_choices)
    choice = input("Please enter your choice [1, 2, 3]: ")
    if choice == "3":
        break
    handel_input(choice)

