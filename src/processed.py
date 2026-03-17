from src.simulation import update_decks, update_counts
from src.storage import load_summary, export_heatmap_csv
from src.viz import create_heatmap
from src.menu import menu
from src.input import user_input
from src.viz_config import compute_viz_atr

sequences = ["BBB", "BBR", "BRB", "BRR", "RBB", "RBR", "RRB", "RRR"]

def processed() -> None:
    '''
    Main entry point. Choose to either to display the most up-to-date heatmaps already generated, 
    or add additional decks, update results, and regenerate heatmaps.
    '''
    while True:
        user_choice = menu()
        
        if user_choice == "1": 
            
            # Loading summaries
            n_t, c_t = load_summary("summary_tricks.npz")
            n_c, c_c = load_summary("summary_cards.npz")

            # Loading in up-to-date heatmap values
            G1WIN, G2WIN, ANNOT1, ANNOT2, MASK1, MASK2 = compute_viz_atr()

            # Current heatmap #1 by original scoring
            create_heatmap(data=G1WIN,
                           title = f"My Chance of Win(Draw)\nTricks\nN={n_t}",
                           x_label = "My Choice",
                           y_label = "Opponent Choice",
                           annot_data=ANNOT1,
                           mask=MASK1)
            
            # Current heatmap #2 by Ron's scoring
            create_heatmap(data=G2WIN,
                           title = f"My Chance of Win(Draw)\nCards\nN={n_c}",
                           x_label = "My Choice",
                           y_label = "Opponent Choice",
                           annot_data=ANNOT2,
                           mask=MASK2)
            
        elif user_choice == "2":
            n_new = user_input()
            if n_new == 0:
                print("No new decks requested.")
                continue
            n_done_tricks, _ = load_summary("summary_tricks.npz")
            start_id = n_done_tricks + 1

            # Update simulation
            decks = update_decks(n_new, start_id)
            update_counts(decks, scoring="tricks")
            update_counts(decks, scoring="cards")

            # Loading summaries
            n_t, c_t = load_summary("summary_tricks.npz")
            n_c, c_c = load_summary("summary_cards.npz")

            # Export heatmap.csv
            export_heatmap_csv(sequences, n_t, c_t, n_c, c_c, filename="heatmap_data.csv")

            # Loading in up-to-date heatmap values
            G1WIN, G2WIN, ANNOT1, ANNOT2, MASK1, MASK2 = compute_viz_atr()

            print("Saved data/heatmap_data.csv")

            # New heatmap #1 by original scoring
            create_heatmap(data=G1WIN,
                           title = f"My Chance of Win(Draw)\nTricks\nN={n_t}",
                           x_label = "My Choice",
                           y_label = "Opponent Choice",
                           annot_data=ANNOT1,
                           mask=MASK1)
            
            # New heatmap #2 by Ron's scoring
            create_heatmap(data=G2WIN,
                           title = f"My Chance of Win(Draw)\nCards\nN={n_c}",
                           x_label = "My Choice",
                           y_label = "Opponent Choice",
                           annot_data=ANNOT2,
                           mask=MASK2)
            
        elif user_choice == "3":
            break
        else:
            print("Invalid option.")