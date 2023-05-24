from src.wordorder_problem.utils import *
n=int(input("Enter the no of words:"))
words=[]
for i in range(n):
    word=input("word:")
    words.append(word)
total_words(n,words)
