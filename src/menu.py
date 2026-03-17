def menu() -> str:
    '''
    Display the main menu and return the user's choice.
    '''
    print("1. Display most up-to-date heatmaps")
    print("2. Simulate additional decks and update results")
    print("3. Exit")
    return input("Choose an option (1-3): ").strip()