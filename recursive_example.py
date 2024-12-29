'''
Recursive functions
'''


def compute_an(n: int):
    '''
    Compute value of a_n defined by the recurence relation a_{n+1} = 2*a_n + 1 and a_0 = 1

    Arg:
        n: int representing the term of sequence
            to compute

    Return:
        int representing the nth term of the sequence

    '''
    if n == 0:
        return 1
    return 2*compute_an(n-1) + 1
