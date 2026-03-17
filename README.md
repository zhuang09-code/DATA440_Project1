# DATA440_Project1_Penny

## Project Overview

This project simulates and visualizes results from the **Humble–Nishiyama (H–N) Randomness Game** using two scoring rules, which is a variation of **[Penney’s Game](https://en.wikipedia.org/wiki/Penney%27s_game)** using a standard 52-card deck represented as 26 red cards ('R') and 26 black cards ('B').

We simulated the game using 3,000,000 randomly generated decks. For each pair of 3-symbol sequences, we estimated the probability of winning or tying under two scoring rules: by tricks (the original H–N version) and by cards won (Ron's variation). The results are summarized in the heatmaps included in this repository.

## Background

Penny's Game is a non-transitive, two-player pattern-matching game on a random binary sequence, meaning there is no single strategy that beats all others. Humble–Nishiyama (H–N) Randomness Game is a variation of Penney’s Game played on a finite shuffled deck instead of an infinite coin-flip sequence.

Both players choose a length-3 sequence from: `BBB, BBR, BRB, BRR, RBB, RBR, RRB, RRR`.

We scan the shuffled deck with a sliding 3-card window:

- If the window matches Player 1’s sequence, Player 1 scores and the matched 3 cards are removed.
- If the window matches Player 2’s sequence, Player 2 scores and the matched 3 cards are removed.
- After a match/removal, scanning restarts from the beginning of the remaining deck.
- The game ends when fewer than 3 cards remain.

We simulate two scoring rules:

- By tricks (original H–N): each match counts as 1 trick.
- By cards won (Ron’s version): each match counts as cards won (under our 3-card match-and-remove rule, each match corresponds to 3 cards).

## How to run the project

from the repository root, run:

```bash
uv run main.py
```

You will be prompted to either:

1. Display most up-to-date heatmaps for 3,000,000 decks
2. Simulate additional decks and update results
3. Exit

If choice 2 is selected, you will be prompted to visualize additional decks along with the 3,000,000 decks to see if any changes occur in the heatmap figures.

## Discussion of findings

Our simulation results show clear patterns in both versions of the game. The heatmaps suggest that no single sequence is always the best choice. Instead, the result depends on which sequence it is matched against. This means the game depends on strategy and counter-strategy, and our results also suggest that Player 2 usually has an advantage because they can respond after seeing Player 1’s choice.

### comparison with original H–N game



### comparison between the two variations


### optimal strategies for players 1 and 2 in each variation