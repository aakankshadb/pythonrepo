from src.minmax_problem.utils import *
row=int(input("Enter the no of rows:"))
columns=int(input("Enter the no of columns:"))
my_array=([])
my_array =np.array([input("Elements:").split() for i in range(row)],int)
minimum(my_array)
