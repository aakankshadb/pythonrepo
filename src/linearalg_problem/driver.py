from src.linearalg_problem.utils import *
n=int(input("Enter the no of rows and elements in array:"))
my_array=([])
my_array=np.array([input("Element:").split() for i in range(n)],float)
determinant(my_array)