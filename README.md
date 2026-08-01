# error-helper-by-delica README
## Purpose
This package simplifies input validation with a suite of functions that check parameter values and 
raise errors (with informative messages printed to stdout) if any user-specified rules are violated
(e.g., submitting a string instead of a float, a negative integer instead of a positive integer,
an empty list instead of a list with multiple valid elements, and many other scenarios that should
generate TypeErrors or ValueErrors).
## Installation
This package is available through the Python Package Index (PyPI).      
One can easily download the package with the following pip install statement:   
`pip install error_helper_by_delica`

If you are a contributor who needs to test changes from the development branch,    
you can install the test version of the library from TestPyPI with the following command:   
`pip install --index-url https://test.pypi.org/simple/error_helper_by_delica`

If you are not a contributor to this project, please only use the production version     
that is deployed on PyPI and can be downloaded with `pip install error_helper_by_delica`.    
The production version is the most stable release of the error helper package.    
## Getting Started
After installation, all we need to start using the package is a function that we want to test.   
For a simple example, we can define a function that returns the opposite of a boolean value.
````
def invert_bool(bool_val):    
    return not bool_val 
````
In its current form, this function does not ensure that the input parameter is a boolean. To protect the function from
unexpected inputs, we can use the error helper library to enforce our boolean type requirement with a single line of
code.
````
import error_helper_by_delica

def invert_bool(bool_val):
    error_helper_by_delica.check_type(bool_val, bool, "boolean parameter")      
    return not bool_val 
````
## Citation
To reference this Python package, please use the following citation.
### APA Format
Leboe-McGowan, D. S. (2026). Error helper by delica (Version 1.0.X) [Source code]. GitHub. 
[https://github.com/DelicaLM/error_helper_by_delica](https://github.com/DelicaLM/error_helper_by_delica)