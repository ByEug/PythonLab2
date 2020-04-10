from math import sqrt


def cashed(function):
    dict_for_args = dict()

    def cashed_decorator(self, *args):
        if dict_for_args.get(args) is None:
            dict_for_args[args] = function(self, *args)
        return dict_for_args[args]

    return cashed_decorator


class Vector:

    def __init__(self, param_list=None):
        if not param_list:
            param_list = [7, 8, 9]
        self.parameters_list = param_list

    def sum_with(self, another_vector):
        buffer = []
        if len(self.parameters_list) == len(another_vector.parameters_list):
            i = 0
            while i < len(self.parameters_list):
                buffer.append(self.parameters_list[i] + another_vector.parameters_list[i])
                i += 1
        else:
            return
        return buffer

    def multiply_on_const(self, multiplier):
        i = 0
        buffer = []
        while i < len(self.parameters_list):
            buffer.append(self.parameters_list[i] * multiplier)
            i += 1
        return buffer

    def subtract_with(self, another_vector):
        buffer = []
        if len(self.parameters_list) == len(another_vector.parameters_list):
            i = 0
            while i < len(self.parameters_list):
                buffer.append(self.parameters_list[i] - another_vector.parameters_list[i])
                i += 1
        else:
            return
        return buffer

    @cashed
    def scalar_multiplication(self, another_vector):
        buffer = 0
        if len(self.parameters_list) == len(another_vector.parameters_list):
            for item_self, item_add in zip(self.parameters_list, another_vector.parameters_list):
                buffer += (item_self * item_add)
        else:
            return
        return buffer

    def is_equal(self, another_vector):
        equal = True
        if len(self.parameters_list) == len(another_vector.parameters_list):
            for item_self, item_add in zip(self.parameters_list, another_vector.parameters_list):
                if item_self != item_add:
                    equal = False
        else:
            equal = False
            return equal
        return equal

    def vector_length(self):
        length = 0
        for item in self.parameters_list:
            length += item**2
        length = sqrt(length)
        return length

    def element(self, index):
        if len(self.parameters_list) <= index:
            return print("There is no such element")
        else:
            i = 0
            while i < len(self.parameters_list):
                if i == index:
                    return self.parameters_list[i]
                i += 1

    def vector_string(self):
        str_buffer = "("
        for item in self.parameters_list:
            if str_buffer == "(":
                str_buffer += str(item)
            else:
                str_buffer = str_buffer + ", " + str(item)
        str_buffer += ")"
        return str_buffer


the_first_vector = Vector([2, 3, 4])
the_second_vector = Vector([5, 6, 7])
print(the_first_vector.parameters_list)
print(the_second_vector.parameters_list)
the_sum_vector = Vector(the_first_vector.sum_with(the_second_vector))
print("Sum: " + str(the_sum_vector.parameters_list))
the_diff_vector = Vector(the_first_vector.subtract_with(the_second_vector))
print("Diff: " + str(the_diff_vector.parameters_list))
the_mult_vector = Vector(the_first_vector.multiply_on_const(2))
print(the_mult_vector.parameters_list)
print(the_first_vector.vector_length())
print(the_first_vector.vector_string())
print(the_first_vector.element(3))
print(the_first_vector.is_equal(the_first_vector))
print(the_first_vector.scalar_multiplication(the_first_vector))
