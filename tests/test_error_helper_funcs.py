"""Script to test the functions in the test helper package (error_helper_funcs.py)."""

import error_helper_by_delica as error_lib
import test_helper_by_delica as test_lib
from test_helper_by_delica.IOPair import IOPair

import random as rand

LARGE_INT = 100000000
SHORT_LIST_LENGTH = 10
LONG_LIST_LENGTH = 250
ATOZ_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ATOZ_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ATOZ_MIXEDCASE = ATOZ_LOWERCASE + ATOZ_UPPERCASE
SHORT_STRING_LENGTH = 5
LONG_STRING_LENGTH = 50

def get_rand_int():
    return rand.randint(-LARGE_INT, LARGE_INT)

def get_rand_pos_int():
    return rand.randint(1, LARGE_INT)

def get_rand_neg_int():
    return rand.randint(-LARGE_INT, 0)

def get_rand_float():
    return 2.0*rand.random()*LARGE_INT - LARGE_INT

def get_rand_pos_float():
    return rand.random()*LARGE_INT

def get_rand_neg_float():
    return -rand.random()*LARGE_INT


def get_rand_int_list(num_ints):
    return [get_rand_int() for i in range(num_ints)]

def get_rand_pos_int_list(num_ints):
    return [get_rand_pos_int() for i in range(num_ints)]

def get_rand_neg_int_list(num_ints):
    return [get_rand_pos_int() for i in range(num_ints)]

def get_rand_letter_lowercase():
    return rand.choice(ATOZ_LOWERCASE)

def get_rand_letter_uppercase():
    return rand.choice(ATOZ_UPPERCASE)

def get_rand_letter_mixedcase():
    return rand.choice(ATOZ_MIXEDCASE)

def get_rand_az_string_lowercase(num_chars):
    result = ""
    for i in range(num_chars):
        result += rand.choice(ATOZ_LOWERCASE)
    return result

def get_rand_az_string_uppercase(num_chars):
    result = ""
    for i in range(num_chars):
        result += rand.choice(ATOZ_UPPERCASE)
    return result

def get_rand_az_string_mixedcase(num_chars):
    result = ""
    for i in range(num_chars):
        result += rand.choice(ATOZ_MIXEDCASE)
    return result

def get_rand_letter_list(list_length):
    return [rand.choice(ATOZ_MIXEDCASE) for i in range(list_length)]

def get_rand_az_string_list(list_length):
    min_string_length = 1
    max_string_length = LONG_STRING_LENGTH
    result = [""]*list_length
    for i in range(list_length):
        string_length = rand.randint(min_string_length, max_string_length+1)
        result[i] = get_rand_az_string_mixedcase(string_length)
    return result








run_all_tests = True
"bool : Boolean flag for whether all tests should be run, regardless of their boolean flags below."

test_check_type = True
"bool : Boolean flag for whether or not to run the tests for the check_type function."
test_check_can_convert = True
"bool : Boolean flag for whether or not to run the tests for the check_can_convert function."
test_check_value_is_in_range = True
"bool : Boolean flag for whether or not to run the tests for the check_value_is_in_range function."
test_check_value_is_in_set = True
"bool : Boolean flag for whether or not to run the tests for the check_value_is_in_set function."


if test_check_type or run_all_tests:
    test_lib.run_func_tests(error_lib.check_type,
        [
        # Test check type on boolean values
        IOPair((True, bool, "true_bool_val"),(True,)),
        IOPair((False, bool, "false_bool_val"),(True,)),
        IOPair((True, int, "true_bool_val"), (TypeError,)),
        IOPair((False, int, "false_bool_val"), (TypeError,)),
        IOPair((True, float, "true_bool_val"), (TypeError,)),
        IOPair((False, float, "false_bool_val"), (TypeError,)),
        IOPair((True, str, "true_bool_val"), (TypeError,)),
        IOPair((False, str, "false_bool_val"), (TypeError,)),
        IOPair((True, list, "true_bool_val"), (TypeError,)),
        IOPair((False, list, "false_bool_val"), (TypeError,)),
        # Test check type on integer values
        IOPair((0, int, "zero_int_val"),(True,)),
        IOPair((0, bool, "zero_int_val"),(TypeError,)),
        IOPair((0, float, "zero_int_val"),(TypeError,)),
        IOPair((1, int, "one_int_val"),(True,)),
        IOPair((1, bool, "one_int_val"),(TypeError,)),
        IOPair((-1, int, "negone_int_val"),(True,)),
        IOPair((get_rand_pos_int(), int, "rand_pos_int_val"), (True,)),
        IOPair((get_rand_pos_int(), float, "rand_pos_int_val"), (TypeError,)),
        IOPair((get_rand_pos_int(), str, "rand_pos_int_val"), (TypeError,)),
        IOPair((get_rand_neg_int(), int, "rand_neg_int_val"),(True,)),
        IOPair((get_rand_neg_int(), float, "rand_neg_int_val"),(TypeError,)),
        IOPair((get_rand_neg_int(), str, "rand_neg_int_val"),(TypeError,)),
        # Test check type on floats
        IOPair((0.0, float, "zero_float_val"), (True,)),
        IOPair((1.0, float, "pos_one_float_val"), (True,)),
        IOPair((-1.0, float, "neg_one_float_val"), (True,)),
        IOPair((get_rand_pos_float(), float, "rand_pos_float_val"), (True,)),
        IOPair((get_rand_neg_float(), float, "rand_neg_float_val"), (True,)),
        IOPair((0.0, int, "zero_float_val"), (TypeError,)),
        IOPair((get_rand_float(), int, "rand_float_val"), (TypeError,)),
        IOPair((get_rand_float(), str, "rand_float_val"), (TypeError,)),
        IOPair((get_rand_float(), list, "rand_float_val"), (TypeError,)),
        # Test check type on strings
        IOPair(("", str, "empty_string_val"), (True,)),
        IOPair((get_rand_letter_lowercase(), str, "rand_lowercase_letter_val"), (True,)),
        IOPair((get_rand_letter_uppercase(), str, "rand_uppercase_letter_val"), (True,)),
        IOPair((get_rand_az_string_lowercase(SHORT_STRING_LENGTH), str, "rand_lowercase_short_az_string_val"),
               (True,)),
        IOPair((get_rand_az_string_uppercase(SHORT_STRING_LENGTH), str, "rand_uppercase_short_az_string_val"),
               (True,)),
        IOPair((get_rand_az_string_mixedcase(SHORT_STRING_LENGTH), str, "rand_mixedcase_short_az_string_val"),
               (True,)),
        IOPair((get_rand_az_string_mixedcase(LONG_STRING_LENGTH), str, "rand_mixedcase_long_az_string_val"),
               (True,)),
        IOPair(("", bool, "empty_string_val"), (TypeError,)),
        IOPair(("", int, "empty_string_val"), (TypeError,)),
        IOPair(("", float, "empty_string_val"), (TypeError,)),
        IOPair(("", list, "empty_string_val"), (TypeError,)),
        IOPair((get_rand_letter_mixedcase(), bool, "rand_mixedcase_letter_val"),
               (TypeError,)),
        IOPair((get_rand_letter_mixedcase(), int, "rand_mixedcase_letter_val"),
               (TypeError,)),
        IOPair((get_rand_letter_mixedcase(), float, "rand_mixedcase_letter_val"),
               (TypeError,)),
        IOPair((get_rand_letter_mixedcase(), list, "rand_mixedcase_letter_val"),
               (TypeError,)),
        IOPair((get_rand_az_string_mixedcase(LONG_STRING_LENGTH), bool, "rand_mixedcase_long_az_string_val"),
                (TypeError,)),
        IOPair((get_rand_az_string_mixedcase(LONG_STRING_LENGTH), int, "rand_mixedcase_long_az_string_val"),
               (TypeError,)),
        IOPair((get_rand_az_string_mixedcase(LONG_STRING_LENGTH), float, "rand_mixedcase_long_az_string_val"),
               (TypeError,)),
        IOPair((get_rand_az_string_mixedcase(LONG_STRING_LENGTH), list, "rand_mixedcase_long_az_string_val"),
                (TypeError,)),
        # Test check type on lists
        IOPair(([], list, "empty_list"), (True,)),
        IOPair(([get_rand_int()], list, "single_int_list"), (True,)),
        IOPair((get_rand_int_list(SHORT_LIST_LENGTH), list, "short_int_list"), (True,)),
        IOPair(([], bool, "empty_list"), (TypeError,)),
        IOPair(([], int, "empty_list"), (TypeError,)),
        IOPair(([], float, "empty_list"), (TypeError,)),
        IOPair(([], str, "empty_list"), (TypeError,)),
        IOPair(([get_rand_int()], bool, "single_int_list"), (TypeError,)),
        IOPair(([get_rand_int()], int, "single_int_list"), (TypeError,)),
        IOPair(([get_rand_int()], float, "single_int_list"), (TypeError,)),
        IOPair(([get_rand_int()], str, "single_int_list"), (TypeError,)),
        IOPair((get_rand_int_list(SHORT_LIST_LENGTH), bool, "short_int_list"), (TypeError,)),
        IOPair((get_rand_int_list(SHORT_LIST_LENGTH), int, "short_int_list"), (TypeError,)),
        IOPair((get_rand_int_list(SHORT_LIST_LENGTH), float, "short_int_list"), (TypeError,)),
        IOPair((get_rand_int_list(SHORT_LIST_LENGTH), str, "short_int_list"), (TypeError,)),
        ])


if test_check_can_convert or run_all_tests:
    test_lib.run_func_tests(error_lib.check_can_convert,[
                # Test can convert on an integer of value zero
                IOPair((0, int, "zero_int_val"),(True,)),
                IOPair((0,float, "zero_int_val"),(True,)),
                IOPair((0,str, "zero_int_val"),(True,)),
                IOPair((0, list, "zero_int_val"), (TypeError,)),
                # Test can convert on a random positive integer
                IOPair((get_rand_pos_int(), int, "rand_pos_int_val"), (True,)),
                IOPair((get_rand_pos_int(), float, "rand_pos_int_val"), (True,)),
                IOPair((get_rand_pos_int(), str, "rand_pos_int_val"), (True,)),
                IOPair((get_rand_pos_int(), list, "rand_pos_int_val"), (TypeError,)),
                # Test can convert on a random negative integer
                IOPair((get_rand_neg_int(), int, "rand_neg_int_val"), (True,)),
                IOPair((get_rand_neg_int(), float, "rand_neg_val"), (True,)),
                IOPair((get_rand_neg_int(), str, "rand_neg_int_val"), (True,)),
                IOPair((get_rand_neg_int(), list, "rand_neg_int_val"), (TypeError,)),
                # Test can convert on floats
                # Test can convert on strings
                # Test can convert on list variables
                IOPair(([], list, "empty_list"), (True,)),
                IOPair(([get_rand_int()], list, "single_rand_int_list"), (True,)),
                IOPair((get_rand_int_list(LONG_LIST_LENGTH), list, "long_int_list"), (True,)),
                IOPair(([], int, "empty_list"), (TypeError,)),
                IOPair(([], str, "empty_list"), (True,)),
                IOPair(([get_rand_int()], str, "single_rand_int_list"), (True,)),
                IOPair((get_rand_int_list(LONG_LIST_LENGTH), list, "long_int_list"), (True,)),
                ])

#if test_check_type or run_all_tests:

#
# class Test(TestCase):
#     def test_check_type(self):
#         test_lib.test_bool_func(self, error_helper.check_type,
#                        [(5, int, "integer variable"),
#                         (5.0, float, "float variable"),
#                         (True, bool, "boolean variable"),
#                         (False, bool, "boolean variable"),
#                         ("", str, "empty string variable"),
#                         ("t", str, "single-character string variable"),
#                         ("test", str, "multi-character string variable"), ],
#                        [(5.1, int, "float variable"),
#                         (5, float, "int variable"),
#                         (1, str, "int variable"),
#                         (True, str, "bool variable"),
#                         ("", int, "empty string variable"),
#                         ("t", int, "single-character string variable"),
#                         ("test", int, "multi-character string variable"),
#                         ("1", int, "string variable (that contains a number)"), ],
#                        test_desc="type verification function",
#                        error_if_false=True, error_type=TypeError)
#
#     def test_check_value_is_in_set(self):
#         test_lib.test_bool_func(self, error_helper.check_value_is_in_set,
#                        [(1, [1], "single-integer list"),
#                         (1, [1, 2], "two-integer list"),
#                         (2, [1, 2, 3], "three-integer list"),
#                         (-1, [-1, -3, -2], "three-value negative integer list"),
#                         (1, ["1", 2, 1, 4.0, False], "mixed-type list")],
#                        false_inputs=[(2, [1], "single-integer list"),
#                                      (2, [], "empty list"),
#                                      (5, [1, 2, 3], "multi-integer list"),
#                                      (2, ["string1","string2", "2"], "multi-string list with number string")],
#                        test_desc="value in set verification function",
#                        error_if_false=True, error_type=ValueError)
#
#     def test_check_value_is_in_range(self):
#         test_lib.test_bool_func(self, error_helper.check_value_is_in_range,
#                        true_inputs=[(1, 1, 1, "single-value int inclusive range"),
#                                     (2, 1, 3, "three-value int inclusive range"),
#                                     (2, 1, 3, "three-value int exclusive range", False, False),
#                                     (2, 1.0, 3.0, "three-value float inclusive range"),
#                                     (2, 1.0, 3.0, "three-value float exclusive range", False, False),
#                                     (1, 1, 3, "three-value min inclusive max exclusive int range", True, False),
#                                     (3, 1, 3, "three-value min exclusive max inclusive int range", False, True),
#                                     (-2, -3, -1, "three-value negative int range"),
#                                     (-2, -3, -1, "three-value negative int exclusive range"),
#                                     (-3, -3, -1, "three-value min inclusive max exclusive negative int range"),
#                                     (-1, -3, -1, "three-value min exclusive max inclusive negative int range"),
#                                     ("a", "a", "a", "single-value string range"),
#                                     ("b", "a", "c", "three-value string range"),
#                                     ("b", "a", "c", "three-value string exclusive range", False, False), ],
#                        false_inputs=[(0, 1, 1, "single-value inclusive range"),
#                                      (0, 1, 1, "single-value exclusive range", False, False),
#                                      (1, 1, 1, "single-value exclusive range", False, False), ],
#                        error_if_false=True, error_type=ValueError,
#                        test_desc="value in range verification function", )
#
#     def test_check_can_convert(self):
#         test_lib.test_bool_func(self, error_helper.check_can_convert,
#                        true_inputs=[(1, int, "int-to-int conversion test"),
#                            (1, float, "int-to-float conversion test"),
#                                     (1.0, int, "float-to-int conversion test"),
#                                     (1.5, int, "float with decimal-to-int conversion test"),
#                                     (1.0, float, "float-to-float conversion test"),
#                                     ("1", int, "string number-to-int conversion test"),
#                                     ("string", str, "string-to-string conversion test"),],
#                        false_inputs=[("", int, "empty string-to-int conversion test"),
#                             ("s", int, "single character string-to-int conversion test"),
#                                      ("my_string", int, "multicharacter string-to-int conversion test"),
#                                      ("", float, "empty string-to-int conversion test"),
#                                      ("s", float, "single character string-to-int conversion test"),
#                                      ("my_string", float, "multicharacter string-to-int conversion test")
#                                      ],
#                        error_if_false=True, error_type=TypeError,
#                        test_desc="can convert verification function")
#


