"""Script to test the functions in the test helper package (error_helper_funcs.py)."""

import error_helper_by_delica as error_lib
import test_helper_by_delica as test_lib
from test_helper_by_delica.IOPair import IOPair

import random as rand

from error_helper_by_delica import error_helper_funcs

LARGE_INT = 100000000
SHORT_LIST_LENGTH = 10
LONG_LIST_LENGTH = 250
ATOZ_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ATOZ_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ATOZ_MIXEDCASE = ATOZ_LOWERCASE + ATOZ_UPPERCASE
DIGITS = "0123456789"
MISC_SYMBOLS = "+?/%^&*@!#$()[]{}\'\"\n"
SHORT_STRING_LENGTH = 5
LONG_STRING_LENGTH = 50

def get_rand_bool():
    """Randomly returns True or False with equal probability."""
    return rand.choice([True, False])

def get_rand_bool_list(num_bools):
    """Generates a list with random boolean elements.

    Parameters
    ----------
    num_bools : int
        Length of the list to generate.

    Returns
    -------
    list[bool]
        A list with random boolean elements.
    """
    assert num_bools > 0, "Number of boolean elements must be greater than 0."
    if num_bools <= 0:
        raise ValueError("Number of boolean elements must be greater than 0.")
    return [get_rand_bool() for i in range(num_bools)]

def get_rand_int():
    """Returns a random negative or positive integer."""
    return rand.randint(-LARGE_INT, LARGE_INT)

def get_rand_pos_int():
    """Returns a random positive integer."""
    return rand.randint(1, LARGE_INT)

def get_rand_neg_int():
    """Returns a random negative integer."""
    return rand.randint(-LARGE_INT, 0)

def get_rand_int_list(num_ints):
    """Generates a list with random integer elements.

    Parameters
    ----------
    num_ints : int
        Length of the list to generate.

    Returns
    -------
    list[int]
        A list with random integer elements.
    """
    assert num_ints > 0, "Number of integer elements must be greater than 0."
    if num_ints <= 0:
        raise ValueError("Number of integer elements must be greater than 0.")
    return [get_rand_int() for i in range(num_ints)]

def get_rand_pos_int_list(num_ints):
    """Generates a list with random positive integer elements (>=1).

    Parameters
    ----------
    num_ints : int
        Length of the list to generate.

    Returns
    -------
    list[int]
        A list with random positive integer elements.
        """
    assert num_ints > 0, "Number of integer elements must be greater than 0."
    if num_ints <= 0:
        raise ValueError("Number of integer elements must be greater than 0.")
    return [get_rand_pos_int() for i in range(num_ints)]

def get_rand_neg_int_list(num_ints):
    """Generates a list with random negative integer elements (<=-1).

    Parameters
    ----------
    num_ints : int
        Length of the list to generate.

    Returns
    -------
    list[int]
        A list with random negative integer elements.
        """
    assert num_ints > 0, "Number of integer elements must be greater than 0."
    if num_ints <= 0:
        raise ValueError("Number of integer elements must be greater than 0.")
    return [get_rand_pos_int() for i in range(num_ints)]


def get_rand_float():
    """Returns a random negative or positive floating point number."""
    return 2.0*rand.random()*LARGE_INT - LARGE_INT

def get_rand_pos_float():
    """Returns a random positive floating point number."""
    return rand.random()*LARGE_INT

def get_rand_neg_float():
    """Returns a random negative floating point number."""
    return -rand.random()*LARGE_INT

def get_rand_float_list(num_floats):
    """Generates a list with random positive and negative float elements.

    Parameters
    ----------
    num_floats : floats
        Length of the list to generate.

    Returns
    -------
    list[float]
        A list with random float elements.
    """
    assert num_floats > 0, "Number of float elements must be greater than 0."
    if num_floats <= 0:
        raise ValueError("Number of float elements must be greater than 0.")
    return [get_rand_float() for i in range(num_floats)]

def get_rand_letter_lowercase():
    """Returns a random lowercase a-z letter."""
    return rand.choice(ATOZ_LOWERCASE)

def get_rand_letter_uppercase():
    """Returns a random uppercase A-Z letter."""
    return rand.choice(ATOZ_UPPERCASE)

def get_rand_letter_mixedcase():
    """Returns a random lowercase (a-z) or uppercase (A-Z) letter."""
    return rand.choice(ATOZ_MIXEDCASE)

def get_rand_letter_list(list_length):
    """Generates a list with random positive and negative float elements.

    Parameters
    ----------
    list_length : int
        Length of the list to generate.

    Returns
    -------
    list[str]
        A list with random string elements that each contain a single a-z or A-Z letter.
    """
    assert list_length > 0, "List length must be greater than 0."
    if list_length <= 0:
        raise ValueError("List length must be greater than 0.")
    return [get_rand_letter_mixedcase() for i in range(list_length)]

def get_rand_az_string_lowercase(num_chars):
    """Returns a random string containing only lowercase a-z letters.

    Parameters
    ----------
    num_chars : int
        Length of the string to generate.

    Returns
    -------
    str
        A random string containing only lowercase a-z letters.
    """
    assert num_chars > 0, "String length must be greater than 0."
    if num_chars <= 0:
        raise ValueError("String length float elements must be greater than 0.")
    result = ""
    for i in range(num_chars):
        result += rand.choice(ATOZ_LOWERCASE)
    return result

def get_rand_az_string_uppercase(num_chars):
    """Returns a random string containing only uppercase A-Z letters.

    Parameters
    ----------
    num_chars : int
        Length of the string to generate.

    Returns
    -------
    str
        A random string containing only uppercase A-Z letters.
    """
    result = ""
    for i in range(num_chars):
        result += rand.choice(ATOZ_UPPERCASE)
    return result


def get_rand_az_string_mixedcase(num_chars):
    """Returns a random string upper- and lowercase letters (a-z and A-Z).

    Parameters
    ----------
    num_chars : int
        Length of the string to generate.

    Returns
    -------
    str
        A random string containing uppercase and lowercase letters.
    """
    assert num_chars > 0, "String length must be greater than 0."
    if num_chars <= 0:
        raise ValueError("String length float elements must be greater than 0.")
    result = ""
    for i in range(num_chars):
        result += rand.choice(ATOZ_MIXEDCASE)
    return result

def get_rand_az_string_list(list_length):
    """Generates a list with random string elements that only contain letters in the ranges a-z and A-Z.

    Parameters
    ----------
    list_length : int
        Length of the list to generate.

    Returns
    -------
    list[str]
        A list with random string elements that each contain multiple a-z or A-Z letters.
    """
    assert list_length > 0, "List length must be greater than 0."
    if list_length <= 0:
        raise ValueError("List length must be greater than 0.")
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
        # Test check type on boolean values.
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
        # Test check type on integer values.
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
        # Test check type on floats.
        IOPair((0.0, float, "zero_float_val"), (True,)),
        IOPair((1.0, float, "pos_one_float_val"), (True,)),
        IOPair((-1.0, float, "neg_one_float_val"), (True,)),
        IOPair((get_rand_pos_float(), float, "rand_pos_float_val"), (True,)),
        IOPair((get_rand_neg_float(), float, "rand_neg_float_val"), (True,)),
        IOPair((0.0, int, "zero_float_val"), (TypeError,)),
        IOPair((get_rand_float(), int, "rand_float_val"), (TypeError,)),
        IOPair((get_rand_float(), str, "rand_float_val"), (TypeError,)),
        IOPair((get_rand_float(), list, "rand_float_val"), (TypeError,)),
        # Test check type on an empty string.
        IOPair(("", str, "empty_string_val"), (True,)),
        IOPair(("", bool, "empty_string_val"), (TypeError,)),
        IOPair(("", int, "empty_string_val"), (TypeError,)),
        IOPair(("", float, "empty_string_val"), (TypeError,)),
        IOPair(("", list, "empty_string_val"), (TypeError,)),
        # Test check type on a string that contains one a-z or A-Z letter.
        IOPair((get_rand_letter_lowercase(), str, "rand_lowercase_letter_val"), (True,)),
        IOPair((get_rand_letter_uppercase(), str, "rand_uppercase_letter_val"), (True,)),
        IOPair((get_rand_letter_mixedcase(), bool, "rand_mixedcase_letter_val"),(TypeError,)),
        IOPair((get_rand_letter_mixedcase(), int, "rand_mixedcase_letter_val"),(TypeError,)),
        IOPair((get_rand_letter_mixedcase(), float, "rand_mixedcase_letter_val"),(TypeError,)),
        IOPair((get_rand_letter_mixedcase(), list, "rand_mixedcase_letter_val"),(TypeError,)),
        # Test check type on a short string of random a-z or A-Z letters.
        IOPair((get_rand_az_string_lowercase(SHORT_STRING_LENGTH), str, "rand_lowercase_short_az_string_val"),
               (True,)),
        IOPair((get_rand_az_string_uppercase(SHORT_STRING_LENGTH), str, "rand_uppercase_short_az_string_val"),
               (True,)),
        IOPair((get_rand_az_string_mixedcase(SHORT_STRING_LENGTH), str, "rand_mixedcase_short_az_string_val"),
               (True,)),
        IOPair((get_rand_az_string_mixedcase(LONG_STRING_LENGTH), str, "rand_mixedcase_long_az_string_val"),
               (True,)),
        IOPair((get_rand_az_string_mixedcase(LONG_STRING_LENGTH), bool, "rand_mixedcase_long_az_string_val"),
                (TypeError,)),
        IOPair((get_rand_az_string_mixedcase(LONG_STRING_LENGTH), int, "rand_mixedcase_long_az_string_val"),
               (TypeError,)),
        IOPair((get_rand_az_string_mixedcase(LONG_STRING_LENGTH), float, "rand_mixedcase_long_az_string_val"),
               (TypeError,)),
        IOPair((get_rand_az_string_mixedcase(LONG_STRING_LENGTH), list, "rand_mixedcase_long_az_string_val"),
                (TypeError,)),
        # Test check type on empty lists.
        IOPair(([], list, "empty_list"), (True,)),
        IOPair(([], bool, "empty_list"), (TypeError,)),
        IOPair(([], int, "empty_list"), (TypeError,)),
        IOPair(([], float, "empty_list"), (TypeError,)),
        IOPair(([], str, "empty_list"), (TypeError,)),
        # Test check type on a list with a single boolean value.
        IOPair(([True], list, "single_true_bool_list"), (True,)),
        IOPair(([False], list, "single_false_bool_list"), (True,)),
        IOPair(([True], bool, "single_true_bool_list"), (TypeError,)),
        IOPair(([False], bool, "single_false_bool_list"), (TypeError,)),
        IOPair(([True], int, "single_true_bool_list"), (TypeError,)),
        IOPair(([False], int, "single_false_bool_list"), (TypeError,)),
        IOPair(([True], float, "single_true_bool_list"), (TypeError,)),
        IOPair(([False], float, "single_false_bool_list"), (TypeError,)),
        IOPair(([True], str, "single_true_bool_list"), (TypeError,)),
        IOPair(([False], str, "single_false_bool_list"), (TypeError,)),
        # Test check type on a short list with random boolean elements.
        IOPair((get_rand_bool_list(SHORT_LIST_LENGTH), list, "short_bool_list"), (True,)),
        IOPair((get_rand_bool_list(SHORT_LIST_LENGTH), bool, "short_bool_list"), (TypeError,)),
        IOPair((get_rand_bool_list(SHORT_LIST_LENGTH), int, "short_bool_list"), (TypeError,)),
        IOPair((get_rand_bool_list(SHORT_LIST_LENGTH), float, "short_bool_list"), (TypeError,)),
        IOPair((get_rand_bool_list(SHORT_LIST_LENGTH), str, "short_bool_list"), (TypeError,)),
        # Test check type on a list with one random integer.
        IOPair(([get_rand_int()], list, "single_int_list"), (True,)),
        IOPair(([get_rand_int()], bool, "single_int_list"), (TypeError,)),
        IOPair(([get_rand_int()], int, "single_int_list"), (TypeError,)),
        IOPair(([get_rand_int()], float, "single_int_list"), (TypeError,)),
        IOPair(([get_rand_int()], str, "single_int_list"), (TypeError,)),
        # Test check type on a short list with random integer elements.
        IOPair((get_rand_int_list(SHORT_LIST_LENGTH), list, "short_int_list"), (True,)),
        IOPair((get_rand_int_list(SHORT_LIST_LENGTH), bool, "short_int_list"), (TypeError,)),
        IOPair((get_rand_int_list(SHORT_LIST_LENGTH), int, "short_int_list"), (TypeError,)),
        IOPair((get_rand_int_list(SHORT_LIST_LENGTH), float, "short_int_list"), (TypeError,)),
        IOPair((get_rand_int_list(SHORT_LIST_LENGTH), str, "short_int_list"), (TypeError,)),
        # Test check type on a list with one random float.
        IOPair(([get_rand_float()], list, "single_float_list"), (True,)),
        IOPair(([get_rand_float()], bool, "single_float_list"), (TypeError,)),
        IOPair(([get_rand_float()], int, "single_float_list"), (TypeError,)),
        IOPair(([get_rand_float()], float, "single_float_list"), (TypeError,)),
        IOPair(([get_rand_float()], str, "single_float_list"), (TypeError,)),
        # Test check type on a short list with random integer elements.
        IOPair((get_rand_float_list(SHORT_LIST_LENGTH), list, "short_float_list"), (True,)),
        IOPair((get_rand_float_list(SHORT_LIST_LENGTH), bool, "short_float_list"), (TypeError,)),
        IOPair((get_rand_float_list(SHORT_LIST_LENGTH), int, "short_float_list"), (TypeError,)),
        IOPair((get_rand_float_list(SHORT_LIST_LENGTH), float, "short_float_list"), (TypeError,)),
        IOPair((get_rand_float_list(SHORT_LIST_LENGTH), str, "short_float_list"), (TypeError,)),
        # Test check type on a list with one random a-z or A-Z letter element.
        IOPair(([get_rand_letter_mixedcase()], list, "single_letter_list"), (True,)),
        IOPair(([get_rand_letter_mixedcase()], bool, "single_letter_list"), (TypeError,)),
        IOPair(([get_rand_letter_mixedcase()], int, "single_letter_list"), (TypeError,)),
        IOPair(([get_rand_letter_mixedcase()], float, "single_letter_list"), (TypeError,)),
        IOPair(([get_rand_letter_mixedcase()], str, "single_letter_list"), (TypeError,)),
        # Test check type on a short list that contains random a-z or A-Z letters as elements.
        IOPair((get_rand_letter_list(SHORT_LIST_LENGTH), list, "short_letter_list"), (True,)),
        IOPair((get_rand_letter_list(SHORT_LIST_LENGTH), bool, "short_letter_list"), (TypeError,)),
        IOPair((get_rand_letter_list(SHORT_LIST_LENGTH), int, "short_letter_list"), (TypeError,)),
        IOPair((get_rand_letter_list(SHORT_LIST_LENGTH), float, "short_letter_list"), (TypeError,)),
        IOPair((get_rand_letter_list(SHORT_LIST_LENGTH), str, "short_letter_list"), (TypeError,)),
        # Test check type on a list that contains a single short string element.
        IOPair(([get_rand_az_string_mixedcase(SHORT_STRING_LENGTH)], list, "single_az_string_list"),
               (True,)),
        IOPair(([get_rand_az_string_mixedcase(SHORT_STRING_LENGTH)], bool, "single_az_string_list"),
               (TypeError,)),
        IOPair(([get_rand_az_string_mixedcase(SHORT_STRING_LENGTH)], int, "single_az_string_list"),
               (TypeError,)),
        IOPair(([get_rand_az_string_mixedcase(SHORT_STRING_LENGTH)], float, "single_az_string_list"),
               (TypeError,)),
        IOPair(([get_rand_az_string_mixedcase(SHORT_STRING_LENGTH)], str, "single_az_string_list"),
               (TypeError,)),
        # Test check type on a short list that contains random strings as elements.
        IOPair((get_rand_az_string_list(SHORT_LIST_LENGTH), list, "short_az_string_list"),
               (True,)),
        IOPair((get_rand_az_string_list(SHORT_LIST_LENGTH), bool, "short_az_string_list"),
               (TypeError,)),
        IOPair((get_rand_az_string_list(SHORT_LIST_LENGTH), int, "short_az_string_list"),
               (TypeError,)),
        IOPair((get_rand_az_string_list(SHORT_LIST_LENGTH), float, "short_az_string_list"),
               (TypeError,)),
        IOPair((get_rand_az_string_list(SHORT_LIST_LENGTH), str, "short_az_string_list"),
               (TypeError,)),
        # Test check type on type objects.
        IOPair((int, type, "int_type"), (True,)),
        IOPair((int, bool, "int_type"), (TypeError,)),
        IOPair((int, int, "int_type"), (TypeError,)),
        IOPair((int, float, "int_type"), (TypeError,)),
        IOPair((int, str, "int_type"), (TypeError,)),
        IOPair((int, list, "int_type"), (TypeError,)),
        ])


if test_check_can_convert or run_all_tests:
    test_lib.run_func_tests(error_lib.check_can_convert,[
        # Test can convert on booleans.
        IOPair((True, bool, "true_bool"), (True,)),
        IOPair((False, bool, "false_bool"), (True,)),
        IOPair((True, int, "true_bool"), (True,)),
        IOPair((False, int, "false_bool"), (True,)),
        IOPair((True, float, "true_bool"), (True,)),
        IOPair((False, float, "false_bool"), (True,)),
        IOPair((True, str, "true_bool"), (True,)),
        IOPair((False, str, "false_bool"), (True,)),
        IOPair((True, list, "true_bool"), (TypeError,)),
        IOPair((False, list, "false_bool"), (TypeError,)),
        # Test can convert on an integer of value zero.
        IOPair((0, int, "zero_int_val"),(True,)),
        IOPair((0, bool, "zero_int_val"), (True,)),
        IOPair((0,float, "zero_int_val"),(True,)),
        IOPair((0,str, "zero_int_val"),(True,)),
        IOPair((0, list, "zero_int_val"), (TypeError,)),
        # Test can convert on a random positive integer.
        IOPair((get_rand_pos_int(), int, "rand_pos_int_val"), (True,)),
        IOPair((get_rand_pos_int(), bool, "rand_pos_int_val"), (True,)),
        IOPair((get_rand_pos_int(), float, "rand_pos_int_val"), (True,)),
        IOPair((get_rand_pos_int(), str, "rand_pos_int_val"), (True,)),
        IOPair((get_rand_pos_int(), list, "rand_pos_int_val"), (TypeError,)),
        # Test can convert on a random negative integer.
        IOPair((get_rand_neg_int(), int, "rand_neg_int_val"), (True,)),
        IOPair((get_rand_neg_int(), bool, "rand_neg_int_val"), (True,)),
        IOPair((get_rand_neg_int(), float, "rand_neg_val"), (True,)),
        IOPair((get_rand_neg_int(), str, "rand_neg_int_val"), (True,)),
        IOPair((get_rand_neg_int(), list, "rand_neg_int_val"), (TypeError,)),
        # Test can convert on a float of value 0.0.
        IOPair((0.0, float, "zero_float_val"), (True,)),
        IOPair((0.0, int, "zero_float_val"), (True,)),
        IOPair((0.0, bool, "zero_float_val"), (True,)),
        IOPair((0.0, str, "zero_float_val"), (True,)),
        IOPair((0.0, list, "zero_float_val"), (TypeError,)),
        # Test can convert on a random positive float.
        IOPair((get_rand_pos_float(), float, "rand_pos_float_val"), (True,)),
        IOPair((get_rand_pos_float(), int, "rand_pos_float_val"), (True,)),
        IOPair((get_rand_pos_float(), bool, "rand_pos_float_val"), (True,)),
        IOPair((get_rand_pos_float(), str, "rand_pos_float_val"), (True,)),
        IOPair((get_rand_pos_float(), list, "rand_pos_float_val"), (TypeError,)),
        # Test can convert on a random negative float.
        IOPair((get_rand_neg_float(), float, "rand_neg_float_val"), (True,)),
        IOPair((get_rand_neg_float(), int, "rand_neg_float_val"), (True,)),
        IOPair((get_rand_neg_float(), bool, "rand_neg_float_val"), (True,)),
        IOPair((get_rand_neg_float(), str, "rand_neg_float_val"), (True,)),
        IOPair((get_rand_neg_float(), list, "rand_neg_float_val"), (TypeError,)),
        # Test can convert on an empty string.
        IOPair(("", str, "empty_string"), (True,)),
        IOPair(("", list, "empty_string"), (True,)),
        IOPair(("", bool, "empty_string"), (True,)),
        IOPair(("", int, "empty_string"), (TypeError,)),
        IOPair(("", float, "empty_string"), (TypeError,)),
        # Test can convert on a single-character string that contains an a-z or A-Z letter.
        IOPair((get_rand_letter_mixedcase(), str, "single_az_letter"), (True,)),
        IOPair((get_rand_letter_mixedcase(), list, "single_az_letter"), (True,)),
        IOPair((get_rand_letter_mixedcase(), bool, "single_az_letter"), (True,)),
        IOPair((get_rand_letter_mixedcase(), int, "single_az_letter"), (TypeError,)),
        IOPair((get_rand_letter_mixedcase(), float, "single_az_letter"), (TypeError,)),
        # Test can convert on a multi-character string that contains a-z or A-Z letters.
        IOPair((get_rand_az_string_mixedcase(SHORT_STRING_LENGTH), str, "single_az_letter"),
               (True,)),
        IOPair((get_rand_az_string_mixedcase(SHORT_STRING_LENGTH), list, "single_az_letter"),
               (True,)),
        IOPair((get_rand_az_string_mixedcase(SHORT_STRING_LENGTH), bool, "single_az_letter"),
               (True,)),
        IOPair((get_rand_az_string_mixedcase(SHORT_STRING_LENGTH), int, "single_az_letter"),
               (TypeError,)),
        IOPair((get_rand_az_string_mixedcase(SHORT_STRING_LENGTH), float, "single_az_letter"),
               (TypeError,)),
        # Test can convert on an empty list.
        IOPair(([], list, "empty_list"), (True,)),
        IOPair(([], str, "empty_list"), (True,)),
        IOPair(([], bool, "empty_list"), (True,)),
        IOPair(([], int, "empty_list"), (TypeError,)),
        IOPair(([], float, "empty_list"), (TypeError,)),
        # Test can convert on a list with a single integer element.
        IOPair(([get_rand_int()], list, "single_rand_int_list"), (True,)),
        IOPair(([get_rand_int()], str, "single_rand_int_list"), (True,)),
        IOPair(([get_rand_int()], bool, "single_rand_int_list"), (True,)),
        IOPair(([get_rand_int()], int, "single_rand_int_list"), (TypeError,)),
        IOPair(([get_rand_int()], float, "single_rand_int_list"), (TypeError,)),
        # Test can convert on a short list with multiple integer elements.
        IOPair((get_rand_int_list(SHORT_LIST_LENGTH), list, "short_int_list"), (True,)),
        IOPair((get_rand_int_list(SHORT_LIST_LENGTH), str, "short_int_list"), (True,)),
        IOPair((get_rand_int_list(SHORT_LIST_LENGTH), bool, "short_int_list"), (True,)),
        IOPair((get_rand_int_list(SHORT_LIST_LENGTH), int, "short_int_list"),
               (TypeError,)),
        IOPair((get_rand_int_list(SHORT_LIST_LENGTH), float, "short_int_list"),
               (TypeError,)),
        # Test can convert on a long list with multiple integer elements.
        IOPair((get_rand_int_list(LONG_LIST_LENGTH), list, "long_int_list"), (True,)),
        IOPair((get_rand_int_list(LONG_LIST_LENGTH), str, "long_int_list"), (True,)),
        IOPair((get_rand_int_list(LONG_LIST_LENGTH), bool, "long_int_list"), (True,)),
        IOPair((get_rand_int_list(LONG_LIST_LENGTH), int, "long_int_list"),
               (TypeError,)),
        IOPair((get_rand_int_list(LONG_LIST_LENGTH), float, "long_int_list"),
               (TypeError,)),
        # Test can convert on type objects.
        IOPair((int, type, "int_type"), (True,)),
        IOPair((int, bool, "int_type"), (True,)),
        IOPair((int, str, "int_type"), (True,)),
        IOPair((int, int, "int_type"), (TypeError,)),
        IOPair((int, float, "int_type"), (TypeError,)),
        IOPair((int, list, "int_type"), (TypeError,)),
        ])


if test_check_value_is_in_range:
    test_lib.run_func_tests(error_lib.check_value_is_in_range, [
        # Test check in range on integer of value zero.
        IOPair((0, 0, 0, "zero_int"),(True,)),
        IOPair((0, 0, 0, "zero_int", False, True), (ValueError,)),
        IOPair((0, 0, 0, "zero_int", True, False), (ValueError,)),
        IOPair((0, 0, 0, "zero_int", False, False), (ValueError,)),
        # Test check in range on positive integers.
        IOPair((10, 9, 11, "pos_int"), (True,)),
        IOPair((10, 9, 11, "pos_int", False, False), (True,)),
        IOPair((10, 9, 11, "pos_int", False, True), (True,)),
        IOPair((10, 9, 11, "pos_int", True, False), (True,)),
        IOPair((4, 4, 5, "pos_int", True, False), (True,)),
        IOPair((4, 4, 5, "pos_int", False, True), (ValueError,)),
        IOPair((5, 4, 5, "pos_int", False, True), (True,)),
        IOPair((5, 4, 5, "pos_int", True, False), (ValueError,)),
        IOPair((4, 5, 6, "pos_int"), (ValueError,)),
        IOPair((7, 5, 6, "pos_int"), (ValueError,)),
        # Test check in range on negative integers.
        IOPair((-10, -11, -9, "pos_int"), (True,)),
        IOPair((-10, -11, -9, "pos_int", False, False), (True,)),
        IOPair((-10, -11, -9, "pos_int", False, True), (True,)),
        IOPair((-10, -11, -9, "pos_int", True, False), (True,)),
        IOPair((-4, -4, -3, "pos_int", True, False), (True,)),
        IOPair((-4, -4, -3, "pos_int", False, True), (ValueError,)),
        IOPair((-3, -4, -3, "pos_int", False, True), (True,)),
        IOPair((-3, -4, -3, "pos_int", True, False), (ValueError,)),
        IOPair((-4, -6, -5, "pos_int"), (ValueError,)),
        IOPair((-7, -6, -5, "pos_int"), (ValueError,)),
        # Test check in range on float of value zero.
        IOPair((0.0, 0.0, 0.0, "zero_float"), (True,)),
        IOPair((0.0, 0.0, 0.0, "zero_float", False, True, ""), (ValueError,)),
        IOPair((0.0, 0.0, 0.0, "zero_float", True, False, ""), (ValueError,)),
        IOPair((0.0, 0.0, 0.0, "zero_float", False, False, ""), (ValueError,)),
        # Test check in range on positive floats.
        IOPair((10.0, 9.0, 11.0, "pos_float"), (True,)),
        IOPair((10.0, 9.0, 11.0, "pos_float", False, False), (True,)),
        IOPair((10.0, 9.0, 11.0, "pos_float", False, True), (True,)),
        IOPair((10.0, 9.0, 11.0, "pos_float", True, False), (True,)),
        IOPair((4.0, 4.0, 5.0, "pos_float", True, False), (True,)),
        IOPair((4.0, 4.0, 5.0, "pos_float", False, True), (ValueError,)),
        IOPair((5.0, 4.0, 5.0, "pos_float", False, True), (True,)),
        IOPair((5.0, 4.0, 5.0, "pos_float", True, False), (ValueError,)),
        IOPair((4.0, 5.0, 6.0, "pos_float"), (ValueError,)),
        IOPair((7.0, 5.0, 6.0, "pos_float"), (ValueError,)),
        # Test check in range on negative integers.
        IOPair((-10.0, -11.0, -9.0, "pos_float"), (True,)),
        IOPair((-10.0, -11.0, -9.0, "pos_float", False, False), (True,)),
        IOPair((-10.0, -11.0, -9.0, "pos_float", False, True), (True,)),
        IOPair((-10.0, -11.0, -9.0, "pos_float", True, False), (True,)),
        IOPair((-4.0, -4.0, -3.0, "pos_float", True, False), (True,)),
        IOPair((-4.0, -4.0, -3.0, "pos_float", False, True), (ValueError,)),
        IOPair((-3.0, -4.0, -3.0, "pos_float", False, True), (True,)),
        IOPair((-3.0, -4.0, -3.0, "pos_float", True, False), (ValueError,)),
        IOPair((-4.0, -6.0, -5.0, "pos_float"), (ValueError,)),
        IOPair((-7.0, -6.0, -5.0, "pos_float"), (ValueError,)),
        # Test check in range on integers and floats.
        IOPair((2.0, 1, 3,  "pos_float"), (True,)),
        IOPair((2, 1.0, 3, "pos_int"), (True,)),
        IOPair((2, 1, 3.0, "pos_int"), (True,)),
        IOPair((2.0, 4, 3, "pos_float"), (ValueError,)),
        IOPair((2, 4.0, 3, "pos_int"), (ValueError,)),
        IOPair((2, 4, 3.0, "pos_int"), (ValueError,)),
        # Test check in range on single character strings.
        IOPair(('b', 'a', 'c', "single_letter"), (True,)),
        IOPair(('B', 'A', 'C', "single_letter"), (True,)),
        IOPair(('a', 'a', 'c', "single_letter", True, False), (True,)),
        IOPair(('a', 'a', 'c', "single_letter", False, True), (ValueError,)),
        IOPair(('c', 'a', 'c', "single_letter", False, True), (True,)),
        IOPair(('c', 'a', 'c', "single_letter", True, False), (ValueError,)),
        IOPair(('a', 'b', 'c', "single_letter"), (ValueError,)),
        IOPair(('c', 'a', 'b', "single_letter", False, True), (ValueError,)),
        # Test check in range on multi-character strings.
        IOPair(('ab', 'aa', 'ac', "single_letter"), (True,)),
        IOPair(('aB', 'aA', 'aC', "single_letter"), (True,)),
        IOPair(('aa', 'aa', 'ac', "single_letter", True, False), (True,)),
        IOPair(('aa', 'aa', 'ac', "single_letter", False, True), (ValueError,)),
        IOPair(('ac', 'aa', 'ac', "single_letter", False, True), (True,)),
        IOPair(('ac', 'aa', 'ac', "single_letter", True, False), (ValueError,)),
        IOPair(('aa', 'ab', 'ac', "single_letter"), (ValueError,)),
        IOPair(('ac', 'aa', 'ab', "single_letter", False, True), (ValueError,)),
        # Test check in range on boolean values.
        IOPair((True, True, True, "true_bool"), (True,)),
        IOPair((True, False, True, "true_bool"), (True,)),
        IOPair((True, False, False, "true_bool"), (ValueError,)),
        IOPair((True, False, True, "true_bool", False, True), (True,)),
        IOPair((True, False, True, "true_bool", False, False), (ValueError,)),
        IOPair((False, False, False, "false_bool"), (True,)),
        IOPair((False, False, True, "false_bool"), (True,)),
        IOPair((False, False, True, "false_bool", True, False), (True,)),
        IOPair((False, False, True, "false_bool", False, True), (ValueError,)),
        # Test check in range on lists.
        IOPair(([], [], [], "empty_list"), (True,)),
        IOPair(([], [], [], "empty_list", False), (ValueError,)),
        IOPair(([], [], [], "empty_list", True, False), (ValueError,)),
        IOPair(([], [], [], "empty_list", False, False), (ValueError,)),
        IOPair(([2], [1], [3], "one_int_list"), (True,)),
        IOPair(([-2], [-3], [-1], "one_int_list"), (True,)),
        IOPair(([1], [1], [1], "one_int_list", False), (ValueError,)),
        IOPair(([1], [1], [1], "one_int_list", True, False), (ValueError,)),
        IOPair(([2.0], [1.0], [3.0], "one_int_list"), (True,)),
        IOPair(([-2.0], [-3.0], [-1.0], "one_int_list"), (True,)),
        IOPair(([1.0], [1.0], [1.0], "one_int_list", False), (ValueError,)),
        IOPair(([1.0], [1.0], [1.0], "one_int_list", True, False), (ValueError,)),
        IOPair(([1,2], [1,1], [1,3], "two_int_list"), (True,)),
        IOPair(([1,4], [1,1], [1,3], "two_int_list"), (ValueError,)),
        # Test check in range on incorrect parameters.
        IOPair((0, 0, 0, 0), (TypeError,)),
        IOPair((0, 0, 0, "zero_val", 1), (TypeError,)),
        IOPair((0, 0, 0, "zero_val", True, 1), (TypeError,)),
        IOPair((0, 0, 0, "zero_val", True, True, 1), (TypeError,)),
    ])

if test_check_value_is_in_set or run_all_tests:
    test_lib.run_func_tests(error_lib.check_value_is_in_set, [
        # Test check is in set on empty set.
        IOPair((0, [], "zero_int"), (ValueError,)),
        IOPair(("", [], "zero_int"), (ValueError,)),
        IOPair(([], [], "zero_int"), (ValueError,)),
        # Test check is in set on set with one element.
        IOPair((0, [0], "zero_int"), (True,)),
        IOPair((0, [1], "zero_int"), (ValueError,)),
        IOPair(("", [""], "empty_string"), (True,)),
        IOPair(("0", ["1"], "zero_string"), (ValueError,)),
        # Test check is in set on sets with multiple elements.
        IOPair((1, [1, 1, 1], "int_val"), (True,)),
        IOPair((3, [1, 2, 3], "int_val"), (True,)),
        IOPair((4, [1, 2, 3], "int_val"), (ValueError,)),
        IOPair((0, [1, 2, 3], "int_val"), (ValueError,)),
        # Test check is in set on sets that contain lists.
        IOPair(([], [[], [], []], "empty_list"), (True,)),
        IOPair(([], [[1], [2], [3]], "empty_list"), (ValueError,)),
    ])