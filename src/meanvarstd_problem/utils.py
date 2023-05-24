import numpy as np
def mean_func(my_array):
    print(np.mean(my_array, axis =1))
    return(np.mean(my_array, axis =1))
def var_func(my_array):
    print(np.var(my_array, axis =0))
    return(np.var(my_array, axis =0))
def std_func(my_array):
    print(round(np.std(my_array),11))
    return(round(np.std(my_array),11))