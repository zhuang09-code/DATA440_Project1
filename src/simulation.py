import numpy as np
import os
from src.deck import generate_deck
from src.game import play_game
from src.storage import save_data, load_summary, save_summary

sequences = ["BBB", "BBR", "BRB", "BRR", "RBB", "RBR", "RRB", "RRR"]

def update_decks(n_new: int, start_id: int) -> np.ndarray:
    '''
    Generate n_new new decks, save them to disk once, and return them as a numpy array, 
    which has the shape (n_new, 52) containing 'R'/'B' values for each deck.
    If n_new == 0, returns an empty array of shape (0, 52).

    Required arguments
    n_new: an int, the number of new random decks to generate.
    start_id: an int, the starting deck id used for naming the saved file. Must be >= 1.
    '''

    if n_new < 0:
        raise ValueError("Number of new decks must be non-negative.")
    if start_id < 1: 
        raise ValueError("start_id must be >= 1.")
    if n_new == 0: 
        return np.empty((0, 52), dtype=str)
    
    # Generate new decks
    deck_list = []
    for _ in range(n_new):
        deck = generate_deck()
        deck_list.append(deck)
    decks = np.array(deck_list)

    # Save raw decks
    end_id = start_id + n_new - 1
    filename = f"decks_{start_id:07d}_to_{end_id:07d}.npy"
    save_data(decks, filename)
    return decks

def update_counts(decks: np.ndarray, scoring: str = "tricks") -> None: 
    '''
    Update cumulative win/draw/loss counts for the given scoring rule using provided decks.
    Saves results to summary_{scoring}.npz.

    Required argument
    decks: a numpy.ndarray, array of decks with shape (n_new, 52).

    Optional argument
    scoring: a str, "tricks" for original H-N scoring, or "cards" for Ron's scoring.
    '''

    if scoring not in ("tricks", "cards"):
        raise ValueError("scoring must be either 'tricks' or 'cards'.")
    if not isinstance(decks, np.ndarray):
        raise TypeError("decks must be a numpy array.")
    if decks.size == 0:
        return
    
    # Use separate summaries for different scoring rules
    summary_name = f"summary_{scoring}.npz"
    # Load previous summary
    n_done, counts = load_summary(summary_name)

    # Update counts using new decks
    for deck in decks: 
        for i in range(len(sequences)):
            p1 = sequences[i]
            for j in range(len(sequences)):
                p2 = sequences[j]
                p1_score, p2_score = play_game(deck, p1, p2, scoring=scoring)
                if p1_score > p2_score:
                    counts[i, j, 0] += 1
                elif p1_score == p2_score:
                    counts[i, j, 1] += 1
                else:
                    counts[i, j, 2] += 1

    # Save updated summary
    save_summary(n_done + len(decks), counts, summary_name)