import random

DEF_DIFFIC = 10
MAX_TRIALS = 20
MAX_VALUE = 99
OPERATORS = "+-*%"
EQUALITY = "="
DIGITS = "0123456789"
NOT_POSSIBLE = "No FoCdle found of that difficulty"

def create_secret(difficulty=DEF_DIFFIC):
    count = 0
    '''This function attempts to generate a random FoCdle instance of a 
    certain length under a maximum number of attempts.'''
    # This will try to create a secret for as many tries as the max trials
    while count != int(MAX_TRIALS):
        
        # This code generates the possible secret string
        possible_focdle = ""
        possible_focdle += str(random.randint(1, MAX_VALUE + 1))
        possible_focdle += random.choice(list(OPERATORS))
        possible_focdle += str(random.randint(1, MAX_VALUE + 1))
        possible_focdle += random.choice(list(OPERATORS))
        possible_focdle += str(random.randint(1, MAX_VALUE + 1))
        possible_ans = eval(possible_focdle)
        possible_focdle += str(EQUALITY)
        possible_focdle += str(possible_ans)
        
        # This code checks if the answer to the equation is positive
        if len(possible_focdle) == difficulty:
            
            # If the answer is positive, the possible focdle is accepted
            if possible_ans > 0:
                return possible_focdle
        else:
            count += 1
            
    # After a max number of unsuccessful trials, this message is returned       
    return "No FoCdle found of that difficulty"




        
    
    