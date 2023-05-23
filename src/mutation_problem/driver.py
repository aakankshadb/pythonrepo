from src.mutation_problem.utils import *
print("Enter the string:")
string=input()
print("Enter the character:")
character=input()
print("Enter the position:")
position=input()
new_string=mutate_string(string,position,character)
print(new_string)
