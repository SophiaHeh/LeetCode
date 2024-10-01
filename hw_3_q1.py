
import numpy as np
def run_simulation(num_exp):
    '''
    Estimate the probabilities of Double six in 24 throws vs One six in 4 throws
    
     Args:
        num_exp: Number of simulation experiments to perform
        
    Returns:
    tuple: (prob_double_six, prob_single_six)
           - prob_double_six: The probability of getting at least one double six in 24 throws of a pair of dice.
           - prob_single_six: The probability of getting at least one six in 4 throws of a single die.
    ''' 


    #Success case for getting at least one double six in 24 throws
    double_six = 0
    
    for _ in range(num_exp):
        is_success = False #Reset is_success to False at the beginning of each experiment(注意不是放在最外面！每一次都要reset!容易錯)
        die1_roll = np.random.randint(1, 7, 24) #roll for first die 24 times #rolling dice是一個動作
        die2_roll = np.random.randint(1, 7, 24) #roll for second die 24 times 
    
        for i in range(24):
            if die1_roll[i] == 6 and die2_roll[i] == 6: #one double six happends
                is_success = True 
                break #exit loop early since we already found a double six
        if is_success:
            double_six += 1

    prob_double_six = double_six / num_exp

    

    #Success case for getting at least one six in 4 throws of a single die
    single_six = 0

    for _ in range(num_exp):
        rolls = np.random.randint(1, 7, 4) #roll the die 4 times
        if 6 in rolls:
            single_six += 1
        
    prob_single_six = single_six / num_exp
    
    return prob_double_six, prob_single_six

#注意題目中的relevant relative frequencies 就是“相對頻率”也就是計算這個“ prob_single_six = single_six / num_exp”

prob_double_six, prob_single_six = run_simulation(10)
print(f"Number of Experiments: {10}")
print(f"Probability of getting at least one double six in 24 throws: {prob_double_six:.4f}")
print(f"Probability of getting at least one six in 4 throws: {prob_single_six:.4f}")
print()  # Print a new line for better readability

prob_double_six, prob_single_six = run_simulation(100)
print(f"Number of Experiments: {100}")
print(f"Probability of getting at least one double six in 24 throws: {prob_double_six:.4f}")
print(f"Probability of getting at least one six in 4 throws: {prob_single_six:.4f}")
print()  # Print a new line for better readability

prob_double_six, prob_single_six = run_simulation(1000)
print(f"Number of Experiments: {1000}")
print(f"Probability of getting at least one double six in 24 throws: {prob_double_six:.4f}")
print(f"Probability of getting at least one six in 4 throws: {prob_single_six:.4f}")


