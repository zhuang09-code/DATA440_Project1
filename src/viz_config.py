import numpy as np
import pandas as pd

def compute_viz_atr(csv_path="data/heatmap_data.csv"):
    df = pd.read_csv(csv_path)

    # Original game
    G1WIN = df.pivot(index="seq_b",
                     columns="seq_a",
                     values="trick_win_pct").values

    G1TIE = df.pivot(index="seq_b",
                     columns="seq_a",
                     values="trick_tie_pct").values

    # Ron's game
    G2WIN = df.pivot(index="seq_b",
                     columns="seq_a",
                     values="card_win_pct").values

    G2TIE = df.pivot(index="seq_b",
                     columns="seq_a",
                     values="card_tie_pct").values

    MASK1 = np.eye(G1WIN.shape[0], dtype=bool) # Mask for original game
    MASK2 = np.eye(G2WIN.shape[0], dtype=bool) # Mask for Ron's game

    # Annotation matrix for original game
    ANNOT1 = np.empty(G1WIN.shape, dtype=object)
    for i in range(G1WIN.shape[0]):
        for j in range(G1WIN.shape[1]):
            ANNOT1[i, j] = f'{G1WIN[i, j]}({G1TIE[i, j]})'
    
    # Annotation matrix for Ron's game
    ANNOT2 = np.empty(G2WIN.shape, dtype=object)
    for i in range(G2WIN.shape[0]):
        for j in range(G2WIN.shape[1]):
            ANNOT2[i, j] = f'{G2WIN[i, j]}({G2TIE[i, j]})'

    return G1WIN, G2WIN, ANNOT1, ANNOT2, MASK1, MASK2