import numpy as np

class ZeroSumGame:
    def __init__(self, game_matr):
        """
        Initializes the game with a payoff matrix.
        """
        self.game_matr = np.array(game_matr)

    def _check_constant_sum(self):
        """
        Private method to check if the matrix represents a zero-sum OR constant-sum game.
        """
        # Get the sum of the very first cell to use as our reference sum (e.g., 0 or 100)
        ref_sum = self.game_matr[0, 0][0] + self.game_matr[0, 0][1]
        
        for i in range(self.game_matr.shape[0]):
            for j in range(self.game_matr.shape[1]):
                if self.game_matr[i, j][0] + self.game_matr[i, j][1] != ref_sum:
                    return False
        return True 

    def _comp_saddle_point(self):
        """
        Private method to compute the saddle point indices.
        """
        if self._check_constant_sum():
            red_matrix = self.game_matr[:, :, 0]
            min_in_rows = np.min(red_matrix, axis=1)
            max_in_cols = np.max(red_matrix, axis=0)
            saddle_points = []
            
            for i in range(red_matrix.shape[0]):
                for j in range(red_matrix.shape[1]):
                    if red_matrix[i, j] == min_in_rows[i] and red_matrix[i, j] == max_in_cols[j]:
                        saddle_points.append((i, j))
            return saddle_points
        else:
            return None

    def get_saddle_point_idx(self):
        """
        Public method to get the index of the saddle points.
        """
        saddle_idx = self._comp_saddle_point()
        return saddle_idx if saddle_idx else "No saddle points found / No pure strategies found / Not a Zero-sum Game / Not a constant-sum game."

    def get_saddle_points(self):
        """
        Public method to get the payoffs at the saddle points.
        """
        saddle_idx = self._comp_saddle_point()
        saddle_points = [self.game_matr[i, j] for i, j in saddle_idx] if saddle_idx else []
        
        if saddle_points:
            return f"Saddle points (payoffs): {saddle_points}"
        else:
            return "Saddle points (payoffs): No saddle points found / No pure strategies found."
