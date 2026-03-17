import numpy as np

def generate_deck() -> np.ndarray: 
    '''
    Return a shuffled 52-card deck consisting of 26 'R' cards and 26 'B' cards.
    '''
    deck = np.array(['R'] * 26 + ['B'] * 26)
    np.random.shuffle(deck)
    return deck