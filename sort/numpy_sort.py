import numpy as np

from common.helpers import default_compare

def sort(array, compare=default_compare):
    if compare == default_compare:
        return list(np.sort(array))
    else:
        return list(np.sort(array)[::-1])