from src.meanvarstd_problem.utils import *
n=int(input("Enter the no of rows:"))
m =int(input("Enter the no of elements in each row:"))
my_array=([])
my_array = np.array([input("Element:").split() for i in range(n)],float)
mean_func(my_array)
var_func(my_array)
std_func(my_array)

