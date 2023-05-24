from src.noidea_problem.utils import *
n=int(input("Enter the no of lines:"))
m=int(input("Enter the no of elements of set:"))
elements = list(map(int, input("Element for list:").split()))
A = set(map(int, input("Elements for set A:").split()))
B = set(map(int, input("Elements for set B:").split()))
happiness_calc(elements,A,B)