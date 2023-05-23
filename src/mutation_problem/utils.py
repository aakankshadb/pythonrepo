def mutate_string(string, position, character):
    lis=[x for x in string]
    #print(lis)
    lis[int(position)]=character
    #print(lis)
    new_str=''.join(lis)
    return new_str
