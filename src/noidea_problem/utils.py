def happiness_calc(elements,A,B):
    happiness = 0
    for element in elements:
        if element in A:
            happiness += 1
        elif element in B:
            happiness += -1
    print(happiness)
    return(happiness)
