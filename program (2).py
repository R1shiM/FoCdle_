GREEN = "green"
YELLO = "yellow"
GREYY = "grey"

def passes_restrictions(guess, all_info):
    '''This code checks if a new guess suggested by the player violates
    the information that has already been collected in 'all_info'.'''
    
    
    # This code checks the positional constraints
    i = 0
    for character in guess:
        
        for info in all_info:
            
            # If a green match exists 
            if (info[i][2] == GREEN) and character != info[i][1]:
                # Only the corresponding character can occur
                return False
            
            # A corresponding character can't occur here without a green match
            elif (info[i][2] == YELLO or info[i][2] == GREYY) and \
                character == info[i][1]:
                
                return False
            
        i += 1
    
     
    # This code checks the distributional constraints
    for info in all_info:
        
        counting_dict = dict()
        tot_grey = 0
        freq = dict()
        
        for char in guess:
            freq[char] = 0
         
        
        for char in guess:
            # This checks the frequency of each character in the guess
            freq[char] += 1
            
             
            tot_grey = 0
            
            # Counts how many times characters are tagged as each colour
            counting_dict[char + GREEN] = 0
            counting_dict[char + YELLO] = 0
            counting_dict[char + GREYY] = 0
            for each_info in info:
                if each_info[1] == char:
                    counting_dict[char + each_info[2]] += 1
                if each_info[2] == GREYY:
                    # Also checks the total number of grey tags
                    tot_grey += 1
                    
        for char in guess:            
            # Characters can't appear less than the number of green and yellow
            # tags they receive
            if freq[char] < counting_dict[char + GREEN] \
                + counting_dict[char + YELLO]:
                
                return False
            
            # Characters can't appear more than their max green + yellow tags
            if counting_dict[char + GREYY] != 0:
                if freq[char] > counting_dict[char + GREEN] \
                                 + counting_dict[char + YELLO]:
                    
                    return False
                
            # Characters can't appear more than their max green + yellow tags 
            # + the total number of grey tags
            if counting_dict[char + GREYY] == 0:
                if freq[char] >> tot_grey + counting_dict[char + GREEN] \
                                              + counting_dict[char + YELLO]:
                    
                    return False
    return True    

    