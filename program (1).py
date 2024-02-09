from collections import defaultdict
GREEN = "green"
YELLO = "yellow"
GREYY = "grey"

def set_colors(secret, guess):
    '''This compares the current guess with the secret and for each position,
    returns either: green (correct character and position), yellow (correct 
    character, wrong position) or grey (incorrect character and position).'''
   
    list_of_colors = []
    
    # This counts the frequency of each character
    counting_dict = defaultdict(int)
    for each_char in secret:
        counting_dict[each_char] += 1
    
    counter = 0
    while counter != len(guess):
        current_focus = guess[counter]
        # The color green is awarded if the character is in the guess and
        # in the correct position
        if secret[counter] == current_focus:
            list_of_colors.append((counter, current_focus, GREEN))
        counter += 1
    counter = 0
    while counter != len(guess):
        current_focus = guess[counter]
        if secret[counter] == current_focus:
            pass
        elif counting_dict[current_focus] == 0:
            # If the character isn't in the secret it is tagged as grey.
            list_of_colors.append((counter, current_focus, GREYY))

        elif counting_dict[current_focus] != 0:
            check_for_times = 0
            for tup in list_of_colors:
                if tup[1] == current_focus:
                    check_for_times += 1
            
            if counting_dict[current_focus] > check_for_times:
                # If the color appears but not at that position it is 
                # labelled yellow
                list_of_colors.append((counter, current_focus, YELLO))
                
            else:
                # Unless it appears more times in guess than secret (grey).
                list_of_colors.append((counter, current_focus, GREYY))
                
        counter += 1
        
    return sorted(list_of_colors)

        
    
    


    
    