def searching_random_number(random_number):
           
    """This function finds a random number in a [1,100] range
       by dividing by 2 the whole diapason and searching if 
       the random number higher or lower than desired value."""       
    
    #starting variables:       
    left = 1
    right = 100
               
    while True:
        
        current = (left+right)//2
        
        if current == random_number:
            return(current)
            
        elif random_number > current:
            left = current + 1
            
        else:
            right = current - 1          
            