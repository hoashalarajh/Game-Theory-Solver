# Game Theory Solvers: Minimax & Nash Equilibrium

This repository contains Python scripts for analyzing bi-matrix games and computing pure strategy optimal decisions. The codebase is separated into two distinct solvers to handle different types of competitive and mixed-motive environments, serving as a mathematical foundation for multi-agent decision-making systems.

---

## 📌 Overview

When developing logic for interacting agents, the nature of the environment dictates the appropriate decision-making algorithm. This repository provides separate tools for:

1. **Strictly Competitive Environments (Constant-Sum):** Where one agent's gain is exactly the other agent's loss.
2. **Mixed-Motive Environments (Varying-Sum):** Where agents have independent payoff matrices and can potentially reach mutually beneficial or mutually detrimental outcomes.

---

## 📂 Repository Contents

### 1. `ZeroSumGame.py` (Minimax & Saddle Points)
This script is designed strictly for zero-sum and constant-sum games. It utilizes the **Minimax theorem** to identify pure strategy **Saddle Points**. 

* **Logic:** Assumes agents are in total conflict. The algorithm finds the strategy that minimizes the maximum possible loss.
* **Validation:** Automatically verifies if the input matrix maintains a constant sum across all outcomes before computing.
* **Output:** Returns the matrix indices and payoffs for all pure strategy saddle points.

### 2. `NashEqm.py` (Best Response & Nash Equilibria)
This script handles general non-constant-sum (varying-sum) games, such as the Prisoner's Dilemma. It identifies **Pure Strategy Nash Equilibria** using Best Response logic.

* **Logic:** Assumes agents are maximizing their own individual payoffs. The algorithm identifies states where no agent has an incentive to unilaterally deviate from their chosen strategy.
* **Flexibility:** Can mathematically process both varying-sum and constant-sum matrices (in the latter, the resulting Nash Equilibrium perfectly mirrors the Minimax Saddle Point).

## 🛠️ Prerequisites & Installation

The scripts are written in standard Python and require NumPy for matrix operations.

```bash
pip install numpy
```

---

## 🚀 Usage Examples
### Finding a Saddle Point (Constant-Sum)

```python
from ZeroSumGame import ZeroSumGame

# Payoff matrix (Agent 1, Agent 2)
matrix = [
    [(37, 63), (17, 83), (62, 38)],
    [(47, 53), (60, 40), (52, 48)],
    [(40, 60), (16, 84), (72, 28)]
]

game = ZeroSumGame(matrix)
# getting the indices of saddle points
print(game.get_saddle_point_idx())
# Output: [(1, 0)]
# getting all the saddle points
print(game.get_saddle_points())
# Output: [(47, 53)]
```

### Finding a Nash Equilibrium (Varying-Sum)

```python
from NashEqm import NashEqm

# Prisoner's Dilemma matrix
matrix = [
    [(-1, -1), (-5, 0)],   
    [(0, -5), (-3, -3)]    
]

solver = NashEqm(matrix)
print(solver.get_pure_nash_equilibria())
# Output: [{'Index': (1, 1), 'Payoff': (-3, -3)}]
```

---

## 🎯 Applications

These solvers can be integrated into broader autonomous systems to evaluate baseline deterministic interactions before scaling up to more complex probabilistic models.

---

