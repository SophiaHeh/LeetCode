def drawing_other_nice_figures_part(n: int):
    '''
    Given n, draws depending on the number of lines requested
    
    Arg:
        n: int representing the number of lines requested
        
    Return:
       figures: int representing the figures that we want to represent
    
    '''
    for i in range(1, n+1):
        print((n-1)* " " + i*"*")

drawing_other_nice_figures_part(4)