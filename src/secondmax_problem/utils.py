def second_max(m,lis):
    arr=[]
    max_item=max(lis)
    for i in lis:
         if i!=max_item:
             arr.append(i)
    arr.sort()
    return arr[-1]

