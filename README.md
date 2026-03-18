# DATA440_Project1_Penney

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

From the repository root, run:

```bash
uv run main.py
```

You will be prompted to either:

1. Display most up-to-date heatmaps for 3,000,000 decks
2. Simulate additional decks and update results
3. Exit

If choice 2 is selected, you will be prompted to visualize additional decks along with the 3,000,000 decks to see if any changes occur in the heatmap figures.

## Discussion of findings

Our simulation results show clear patterns in both versions of the game. The heatmaps suggest that no single sequence is always the best choice. Instead, the result depends on which sequence it is matched against. Overall, our results show that the game depends on strategy and counter-strategy, with Player 2 generally having an advantage.

### Comparison with original H–N game

Our results agree with the main conclusions already published for the original H–N game. Like the original game, our simulations show that there is no single sequence that always wins, and Player 2 often can respond with a strong counter because they can choose a counter-sequence after seeing Player 1’s choice. Our heatmaps support this pattern, since each starting sequence has a stronger response from the second player.

### Comparison between the two variations

The two variations produce different heatmaps. For scoring using tricks, each match is worth 1 point, so outcomes depend on how many matches each player gets. For scoring using cards, the winner of a match earns the number of cards consumed up to that match (i.e., i+3 cards), so the value of a match depends on where it occurs in the scan. This changes win and tie probabilities: the cards version generally shows much lower draw rates (often around 0–4%) than the tricks version, and several matchups shift noticeably in win probability.

### Optimal strategies for Player 1 and 2 in each variation

For Player 2, the best response depends on Player 1’s chosen sequence. From each heatmap, Player 2’s optimal counter to a given Player 1 choice can be identified by finding the row that minimizes Player 1’s win probability in that column.

For Player 1, the best strategy is to choose an opening sequence whose worst-case matchup is as strong as possible. This means comparing the minimum Win% in each column and selecting the column with the largest minimum (a maximin-style choice).

