from src.simulation import update_decks, update_counts
from src.storage import load_summary, export_heatmap_csv
import numpy as np
import time

sequences = ["BBB", "BBR", "BRB", "BRR", "RBB", "RBR", "RRB", "RRR"]

if __name__ == "__main__":
    start = time.time()
    decks = update_decks(n_new=3000000, start_id=1)
    update_counts(decks=decks, scoring="tricks")
    update_counts(decks=decks, scoring="cards")
    n_tricks, counts_tricks = load_summary("summary_tricks.npz")
    n_cards, counts_cards = load_summary("summary_cards.npz")
    if n_tricks > 0 and n_cards > 0:
        export_heatmap_csv(
            sequences=sequences,
            n_tricks=n_tricks,
            counts_tricks=counts_tricks,
            n_cards=n_cards,
            counts_cards=counts_cards,
            filename="heatmap_data.csv")
        print("Saved data/heatmap_data.csv")
    else:
        print("No simulation data to export.")

    data_decks = np.load("data/decks_0000001_to_3000000.npy") 
    print(data_decks.shape)
    print(data_decks[0:9])
    print("Time for 1000 decks:", time.time() - start)