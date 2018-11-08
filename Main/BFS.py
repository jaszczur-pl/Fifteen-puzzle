# BFS(breadth-first search) algorithm for 15-puzzle game solver

from queue import PriorityQueue


class BFS:

    def __init__(self, strategy_param, input_values):
        self.strategy_param = strategy_param
        self.rows_number = input_values[0]
        self.columns_number = input_values[1]
        self.puzzle = input_values[2:]

    def solve_puzzle(self):
        print(self.puzzle)
