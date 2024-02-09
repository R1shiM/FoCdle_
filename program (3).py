import random
from hidden import solve_FoCdle

GREEN = "green"
YELLO = "yellow"
GREYY = "grey"
ENABLE_PLAYTEST = False
DEF_DIFFIC = 10
OPERATORS = "+-*%"
EQUALITY = "="
DIGITS = "0123456789"





def create_guess(all_info, difficulty=DEF_DIFFIC):
    '''This function considers the prior information collected in all_info
    and suggests a new guess to solve the FoCdle.'''
    
    # This code initiates the possible characters for each position
    i = 0
    list_of_options = []
    for i in range(difficulty):
        list_of_options.append(set(OPERATORS + EQUALITY + DIGITS))
        i += 1
    
    
    # This updates possible options for each position based off of all_info
    for info in all_info:
        j = 0
        for j in range(difficulty):
            if info[j][2] == GREEN:
                # All other options are removed if this character is correct
                list_of_options[j] = info[j][1]
            else:
                # Only this character is removed from options if it's incorrect
                list_of_options[j].remove(info[j][1])
            j += 1

    # We create a new string that will be the recommended guess
    recommended_guess = ""
    pos = 0
    
    # Each position randomly chooses a character based on remaining options
    for pos in range(difficulty):
        recommended_guess += random.choice(list(list_of_options[pos]))
        pos += 1

    return recommended_guess


# Let's play a game of FoCdle... below we pass your `create_guess` function to
# our hidden `solve_FoCdle` function, which uses it to guess the secret in a
# game of FoCdle. This closely follows the program outline described in task 3.
# You may also call `solve_FoCdle` with `debug=True` to see printed information
# that corresponds with comments in that same outline. 
# 
# Note: When you click "Mark", the `solve_FoCdle` function is run 100 times
# with "25+4*12=73" as the secret, taking the average number of guesses
# required to solve it. The hidden assessment tests will use many different
# random secrets, so make sure you test your code beyond this example!

if ENABLE_PLAYTEST:  # Set to True to run this code when clicking "Run" in Grok
    secret = "25+4*12=73"
    nguesses, final_guess = solve_FoCdle(secret, create_guess, debug=False)
    print(f"Solved the FoCdle after {nguesses} guesses: '{final_guess}'")
