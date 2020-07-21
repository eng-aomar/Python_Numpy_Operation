import numpy as np

class ArrayMathmatics:

    @classmethod
    def add_matrices(cls, array_one, array_two):
        return np.add(array_one, array_one)

    @classmethod
    def subtract_matrices(cls, array_one, array_two):
        return np.subtract(array_one, array_one)

    @classmethod
    def multiply_matrices(cls, array_one, array_two):
        return np.multiply(array_one, array_one)

    @classmethod
    def divide_matrices(cls, array_one, array_two):
        return np.divide(array_one, array_one)

    @classmethod
    def compare_matrices(cls, array_one, array_two):
        return np.array_equal(array_one, array_one)


class ArrayManipulation:

    @classmethod
    def transposing_array(cls,array):
        return np.transpose(array)
    @classmethod    
    def reshape_array(cls, array,rows,columns):
        array.ravel()
        return np.reshape(rows,columns)
    @classmethod
    def combine_arrays(cls, array_one, array_tow, axis=0):
        return np.concatenate((array_one, array_tow),axis)
    @classmethod
    def split_array(cls, array, axis=0):
            return np.array_split(array,)
    


