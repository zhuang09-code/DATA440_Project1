# DATA440_Project1_Penny

## Overview

This project simulates and visualizes results from the **Humble–Nishiyama (H–N) Randomness Game** using two scoring rules, which is a variation of **[Penney’s Game](https://en.wikipedia.org/wiki/Penney%27s_game)** using a standard 52-card deck represented as 26 red cards ('R') and 26 black cards ('B').

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

## Data and data Visualization

We simulated and scored games for random generation of 3,000,000 decks, each with 26 "B" cards and 26 "R" cards.

We report the findings of the probability of win(tie) for one of the 3-lengths equences Vs. the simulation of a choice for another 3-length sequence for both types of scoring rules.

## How to run the project

from the repository root, run:

```bash
uv run main.py
```

You will be prompted to either:

1. Display most up-to-date heatmaps for 3,000,000 decks
2. Simulate additional decks and update results"
3. Exit

If choice 2 is selected, you will be prompted to visualize additional decks along with the 3,000,000 decks to see if any changes occur in the heatmap figures.
