import numpy as np

class NashEqm:
    def __init__(self, game_matr):
        """
        Initializes the game with a payoff matrix.
        Expected format: List of lists of tuples, e.g., [[(p1, p2), (p1, p2)], ...]
        """
        self.game_matr = np.array(game_matr)

    def get_pure_nash_equilibria(self):
        """
        Calculates Pure Strategy Nash Equilibria for general non-constant sum games.
        Returns a list of indices and their corresponding payoffs.
        """
        rows, cols = self.game_matr.shape[:2]
        
        p1_best_responses = set()
        p2_best_responses = set()

        # 1. Find Player 1's best responses (Row player)
        # For every column (Player 2's choice), what is the max payoff for Player 1?
        for j in range(cols):
            col_payoffs_p1 = self.game_matr[:, j, 0]
            max_val_p1 = np.max(col_payoffs_p1)
            for i in range(rows):
                if self.game_matr[i, j, 0] == max_val_p1:
                    p1_best_responses.add((i, j))

        # 2. Find Player 2's best responses (Column player)
        # For every row (Player 1's choice), what is the max payoff for Player 2?
        for i in range(rows):
            row_payoffs_p2 = self.game_matr[i, :, 1]
            max_val_p2 = np.max(row_payoffs_p2)
            for j in range(cols):
                if self.game_matr[i, j, 1] == max_val_p2:
                    p2_best_responses.add((i, j))

        # 3. The intersection of best responses are the Nash Equilibria
        nash_indices = list(p1_best_responses.intersection(p2_best_responses))
        
        if not nash_indices:
            return "No pure strategy Nash Equilibria found."
            
        results = []
        for idx in nash_indices:
            results.append({
                "Index": idx, 
                "Payoff": tuple(self.game_matr[idx[0], idx[1]])
            })
            
        return results
