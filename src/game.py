import numpy as np

def play_game(deck: np.ndarray, p1: str, p2: str, scoring: str = "tricks") -> tuple[int, int]:

    '''
    Simulate one Humble–Nishiyama game using a sliding 3-card window check.
    When a player's 3-card sequence appears, that player scores under the chosen scoring rule, 
    the matched cards are removed, and scanning restarts.
    Returns (p1_score, p2_score). 

    Required arguments
    deck: a numpy.ndarray
        A 1D numpy array representing a shuffled deck of cards, containing only 'R' and 'B'.
    p1: a str
        Player 1's target sequence of length 3, consisting only of 'R' and 'B'.
    p2: a str
        Player 2's target sequence of length 3, consisting only of 'R' and 'B'.

    Optional arguments
    scoring: a str, scoring rule to use
        tricks: original H-N scoring, each match counts as 1 trick
        cards: Ron's scoring, each match counts as the number of cards won.
    '''

    if len(p1) != 3 or len(p2) != 3:
        raise ValueError("Both player sequences must have length 3.")
    if any(c not in ("R", "B") for c in p1 + p2):
        raise ValueError("Sequences must contain only 'R' and 'B'.")
    if scoring not in ("tricks", "cards"):
        raise ValueError("Scoring must be either 'tricks' or 'cards'.")
    
    cards = list(deck)
    p1_list = list(p1)
    p2_list = list(p2)
    p1_score = 0
    p2_score = 0
    i = 0

    while i <= len(cards) - 3:
        check = cards[i:i+3]

        if check == p1_list or check == p2_list:
            k = i + 3  # cards consumed up to and including the match

            if check == p1_list:
                if scoring == "tricks":
                    p1_score += 1
                else:  # scoring == "cards"
                    p1_score += k
            else:  # check == p2_list
                if scoring == "tricks":
                    p2_score += 1
                else:  # scoring == "cards"
                    p2_score += k

            del cards[:k]  # remove consumed prefix
            i = 0
        else:
            i += 1

    return p1_score, p2_score