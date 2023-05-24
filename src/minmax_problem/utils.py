import numpy as np
def minimum(my_array):
    print(np.max(np.min(my_array, axis=1)))
    return (np.max(np.min(my_array, axis=1)))