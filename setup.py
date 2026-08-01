from setuptools import setup
import os

curr_directory = os.path.dirname(os.path.abspath(__file__))
read_me_path = os.path.join(curr_directory, 'README.md')

long_description = ""
try:
    with open(read_me_path, 'r', encoding='utf-8') as read_me_file:
        long_description = read_me_file.read()
except FileNotFoundError:
    pass

required_libraries = []
requirements_path = os.path.join(curr_directory, 'requirements.txt')
try:
    with open(requirements_path, 'r', encoding='utf-8') as requirements_file:
        required_libraries = requirements_file.read().splitlines()
        for i in range(len(required_libraries)):
            required_libraries[i] = required_libraries[i].strip()
except FileNotFoundError:
    pass

test = 0
setup(
    name='error_helper_by_delica',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description="A Python package for checking input parameters and printing informative error messages.",
    author="Delica Leboe-McGowan",
    author_email="stormindustries22@outlook.com",
    packages=['error_helper_by_delica'],
    install_requires=required_libraries,
    long_description=long_description,
    long_description_content_type='text/markdown'
)
