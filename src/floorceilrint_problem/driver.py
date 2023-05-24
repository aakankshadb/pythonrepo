from src.floorceilrint_problem.utils import *

my_array = np.array([])
n=int(input("Enter the no of elements:"))
print("Enter the elements of array:")
for i in range(n):
    x = float(input("Element:"))
    my_array=np.append(my_array,x)
#print(my_array)
floors(my_array)
ceils(my_array)
rints(my_array)




