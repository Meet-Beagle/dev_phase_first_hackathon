#!python3
# stdlib module imports
from datetime import datetime
import warnings
import os

# 3rd party module imports
import numpy as np


def _string_is_empty_or_spaces(string: str):
    return (string is None) or (string == '') or (string.isspace())


def _if_not_exist_mkdir(path: str):
    if _string_is_empty_or_spaces(path):
        warnings.warn('passed path is empty or contains only spaces this might '
                      'lead to errors')
    else:
        if not os.path.exists(path):
            os.makedirs(path)


def _make_filename(path: str = None, name: str = 'empty'):

    if _string_is_empty_or_spaces(path):
        return name
    elif path.strip(' ').endswith('/'):
        return '{0}{1}'.format(path, name)
    else:
        return '{0}/{1}'.format(path, name)


def _timestamp():
    return str(datetime.now()).replace(" ", "_")


def _two_matrix_size_comparison_and_typecheck(m1, m2):
    if np.shape(m1) != np.shape(m2):
        raise ValueError('Shape mismatch. Matrices m1 and m2 must '
                         'have same shapes')
    elif type(m1) != np.ndarray:
        raise TypeError('m1 must be a numpy.ndarray not a {0}'.format(type(m1)))
    elif type(m2) != np.ndarray:
        raise TypeError('m2 must be a numpy.ndarray not a {0}'.format(type(m2)))

if __name__ == '__main__':
    pass