#!/usr/bin/python3
""" Contains lazy_matrix_mul """

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Multiplies 2 matrixes using numpy """
    
    a = np.array(m_a)
    b = np.array(m_b)
    new_m = a.dot(b)
    return new_m
