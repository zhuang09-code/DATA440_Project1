def user_input() -> int:
    '''
    A user input function designed to take in a desired number of samples from the user.
    The function will prompt the user to input an integer for number of samples.
    It will also ask the user if they wish to add more samples.
    '''
    total_samples = 0
    
    while True:
        try:
            num_samples = int(input("Please enter desired number of samples for the simulation: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if num_samples < 0:
            print("Please enter a non-negative integer.")
            continue
        total_samples += num_samples 
        print(f"You entered {num_samples} samples!")
        
        more_samples = input("Would you like to add more samples? (y/n): ")
        if more_samples != 'y':
            break
        
    print(f"\nTotal samples: {total_samples}")
    print("Processing your request...")
    return total_samples