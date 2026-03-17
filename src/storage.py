import numpy as np
import os
import csv

PATH_DATA = 'data'

def save_data(data: np.ndarray, filename: str) -> None:
    '''
    Save a numpy array to the default output folder, 
    ensuring that the folder exists.
    Existing files will not be overwritten.
    '''

    full_filename = os.path.join(PATH_DATA, filename)

    # Ensure the output directory exists
    if not os.path.exists(PATH_DATA):
        os.mkdir(PATH_DATA)
    
    if type(data) != np.ndarray:
        raise TypeError(f'data should be a numpy array, but a {type(data)} was provided.')
    
    # Don't overwrite an existing file
    if os.path.exists(full_filename):
        raise FileExistsError(f'file {full_filename} already exists.')

    # Save the array as a .npy file
    np.save(full_filename, data)
    return None

def load_data(filename: str) -> np.ndarray:
    '''
    Loads data from an .npy file located in the default data directory.
    '''

    full_filename = os.path.join(PATH_DATA, filename)

    # Check file exists
    if not os.path.exists(full_filename):
        raise FileNotFoundError(f'file {full_filename} does not exist.')

    return np.load(full_filename)

def load_summary(summary_filename: str = "summary.npz") -> tuple[int, np.ndarray]:
    '''
    Load cumulative simulation summary.
    Returns (n_decks, counts).
        n_decks: an int, the total number of decks simulated so far.
        counts: a numpy.ndarray, an integer array of shape (8, 8, 3) storing cumulative
        (win, draw, loss) counts for each (p1_strategy, p2_strategy) pair.
    If no summary exists yet, return (0, zeros).
    '''

    summary_file = os.path.join(PATH_DATA, summary_filename)

    if not os.path.exists(summary_file):
        return 0, np.zeros((8, 8, 3), dtype=int)
    
    file = np.load(summary_file)
    n_decks = int(file["n_decks"][0]) 
    counts = file["counts"] 
    return n_decks, counts

def save_summary(n_decks: int, counts: np.ndarray, summary_filename: str = "summary.npz") -> None: 
    '''
    Save cumulative simulation summary.
    counts must have shape (8, 8, 3).

    Required arguments
    n_decks: an int, the total number of decks simulated so far.
    counts: a numpy.ndarray, an integer array of shape (8, 8, 3) storing cumulative
    (win, draw, loss) counts for each (p1_strategy, p2_strategy) pair.
    '''

    if counts.shape != (8, 8, 3):
        raise ValueError(f'counts must have shape (8,8,3), got {counts.shape}')
    
    summary_file = os.path.join(PATH_DATA, summary_filename)

    if not os.path.exists(PATH_DATA):
        os.mkdir(PATH_DATA)

    np.savez_compressed(
        summary_file,
        n_decks=np.array([n_decks]),
        counts=counts
    )

def heatmap_arrays(win_pct: np.ndarray, tie_pct: np.ndarray, filename: str) -> None: 
    '''
    Save final arrays used to generate heatmaps.
    win_pct and tie_pct must have shape (8, 8).
    '''

    if win_pct.shape != (8, 8) or tie_pct.shape != (8, 8):
        raise ValueError("win_pct and tie_pct must both have shape (8, 8).")
    
    array_file = os.path.join(PATH_DATA, filename)
    if not os.path.exists(PATH_DATA):
        os.mkdir(PATH_DATA)

    np.savez_compressed(array_file, win_pct=win_pct, tie_pct=tie_pct)

def export_heatmap_csv(sequences: list[str],
                       n_tricks: int, counts_tricks: np.ndarray,
                       n_cards: int, counts_cards: np.ndarray,
                       filename: str = "heatmap_data.csv",
                       out_dir: str = PATH_DATA,) -> None:
    '''
    Export heatmap-ready data to a CSV with one row per (seq_a, seq_b).
    Columns: seq_a, seq_b, trick_win_pct, trick_tie_pct, card_win_pct, card_tie_pct
    '''
    if counts_tricks.shape != (8, 8, 3) or counts_cards.shape != (8, 8, 3):
        raise ValueError("counts arrays must have shape (8, 8, 3).")
    if n_tricks <= 0 or n_cards <= 0:
        raise ValueError("n_tricks and n_cards must be positive.")
    if len(sequences) != 8:
        raise ValueError("sequences must have length 8.")

    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, filename)

    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["seq_a", "seq_b", "trick_win_pct", "trick_tie_pct", "card_win_pct", "card_tie_pct"])

        for i, a in enumerate(sequences):
            for j, b in enumerate(sequences):
                tw = int(np.rint(100 * counts_tricks[i, j, 0] / n_tricks)) # Compute the probability for win (tricks)
                tt = int(np.rint(100 * counts_tricks[i, j, 1] / n_tricks)) # Compute the probability for tie (tricks)
                cw = int(np.rint(100 * counts_cards[i, j, 0] / n_cards)) # Compute the probability for win (cards)
                ct = int(np.rint(100 * counts_cards[i, j, 1] / n_cards)) # Compute the probability for tie (cards)
                writer.writerow([a, b, tw, tt, cw, ct])