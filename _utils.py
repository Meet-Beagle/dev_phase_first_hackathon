#!python3
# stdlib module imports
from datetime import datetime
import warnings
import os

# 3rd party module imports
import numpy as np
import pyximport

# own Cython module imports
pyximport.install(language_level=3,
                  setup_args={"include_dirs":np.get_include()},
                  reload_support=True)

from genco.pyx_modules import dictator


def _small_data_run(funct):

    number = 18
    n_iter = 20
    sequence_length = 10
    trans_mat = np.array([[0.4, 0.6], [0.4, 0.6]])
    alphabet = np.array(['A', 'B'])
    size_alphabet = np.alen(alphabet)
    numeric_alphabet = np.arange(size_alphabet)
    num_trans_dict = dictator(trans_mat, numeric_alphabet)

    if funct.__name__ is 'sequential_dna_assembly':
        return funct(sequence_length, num_trans_dict, size_alphabet,
                     numeric_alphabet)

    elif funct.__name__ == 'c_sequential_dna_assembly':
        seed = np.empty(sequence_length, dtype=np.int_)
        return funct(seed, sequence_length, num_trans_dict, size_alphabet,
                     numeric_alphabet)

    elif funct.__name__ is 'sequentially_assembled_dna_list':
        return funct(number, sequence_length, trans_mat,
                     size_alphabet, numeric_alphabet, string_output=False)

    elif funct.__name__ == 'c_sequence_list_assembler':
        return funct(number, n_iter, sequence_length, trans_mat,
                     size_alphabet, alphabet, string_output=False)
    else:
        raise ValueError('unknown function was passed, only '
                         'c_sequence_list_assembler, '
                         'sequential_dna_assembly and '
                         'sequentially_assembled_dna_list are supported')


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