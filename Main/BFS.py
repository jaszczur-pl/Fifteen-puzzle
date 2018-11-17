# BFS(breadth-first search) algorithm for 15-puzzle game solver

from queue import Queue
import time
from Main.StrategiesParent import StrategiesParent


class BFS(StrategiesParent):

    def solve_puzzle(self):

        number_of_puzzle_elements = len(self.puzzle)
        frontier = Queue()
        path = Queue()
        frontier.put(tuple(self.puzzle))
        visited_nodes = []
        is_game_solved = False
        sorted_puzzle = self.sort_puzzle(number_of_puzzle_elements)

        start_time = time.time() * 1000

        while not is_game_solved:
            current_node = frontier.get()
            is_game_solved = self.visit_node(current_node, sorted_puzzle)
            visited_nodes.append(current_node)

            if is_game_solved:
                break

            for move_type in self.strategy_param:
                next_node = self.check_possible_moves(move_type, list(current_node[:]))
                if next_node is not None and next_node not in visited_nodes:
                    frontier.put(next_node)
                    path.put(self.solution_path + move_type)

            self.solution_path = path.get()

        end_time = time.time() * 1000

        self.solution_time = round((end_time - start_time), 3)
        self.solution_length = len(self.solution_path)
        self.number_of_visited_nodes = visited_nodes.__len__()
        self.number_of_processed_nodes = frontier.qsize()
        self.recursion_depth = len(self.solution_path)




