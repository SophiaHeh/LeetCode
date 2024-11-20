def compute_a_n(n: int):
    '''
    Compute term of sequence defined by a_{n+1} = 2 a_n +1 
    Arg:
        n: int representing the index of the value of a** to compute
    Return:
        int representing the value of a_n

    '''
    if n == 0:
        return 1
    else:
        if not(n % 2):
            print(f"The value of n is {n}")
        return 2*compute_a_n(n-1) + 1


print(compute_a_n(5))

# T(N) =  # of units of time required to run the function below for an input

#F_n  = F_n-1 + F_n-2
# Write a function which compute a term of the Fibonaccie sequence f_n
# for any n recursilvly


def fib_recursive(n: int):
    '''
    Compute nth Fibonacci number
    Arg:
        n: int representing the index of the Fibonacci number
    Return:
        int representing the nth Fibonacci number

    '''

    # add this code in the begin with the codes,如果不符合條件，直接退出不會進入之後的code
    assert(n >= 0, "n should be non-negative")
    if n < 0:
        return "Input should be non-negative"

    if n == 0 or n == 1: #這個算是3 unit of times, n== 0算一次，n == 1算一次，or 的比較算一次
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


print(fib_recursive(-5))
