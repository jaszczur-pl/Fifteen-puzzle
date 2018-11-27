# DFS(depth-first search) algorithm for 15-puzzle game solver

from queue import LifoQueue
import time
from StrategiesParent import StrategiesParent


class DFS(StrategiesParent):

    def __init__(self, strategy_param, input_values):
        super().__init__(strategy_param, input_values)
        self.max_recursion_depth = 7

    def solve_puzzle(self):

        global current_node
        current_node = tuple(self.puzzle)
        number_of_puzzle_elements = len(self.puzzle)
        frontier = LifoQueue(maxsize=self.max_recursion_depth + 1)
        frontier.put(tuple(self.puzzle))
        path = ''
        visited_nodes = [tuple(self.puzzle)]
        sorted_puzzle = self.sort_puzzle(number_of_puzzle_elements)
        max_recursion_depth = 0
        current_recursion_depth = 0

        start_time = time.time() * 1000

        is_game_solved = self.visit_node(self.puzzle, sorted_puzzle)

        if is_game_solved:
            frontier.get()

        i = 0
        while not is_game_solved:

            if i >= len(self.strategy_param) or frontier.full():
                frontier.get()
                path = path[:-1]
                i = 0
                current_node = frontier.get()
                frontier.put(current_node)

                current_recursion_depth -= 1

            next_node = self.check_possible_moves(self.strategy_param[i], list(current_node[:]))

            if next_node is None or next_node in visited_nodes:
                i += 1
            else:
                path += self.strategy_param[i]
                i = 0
                current_node = next_node
                frontier.put(current_node)

                current_recursion_depth += 1
                if current_recursion_depth > max_recursion_depth:
                    max_recursion_depth = current_recursion_depth

                is_game_solved = self.visit_node(current_node, sorted_puzzle)
                visited_nodes.append(current_node)

            if frontier.qsize() == 1 and i >= len(self.strategy_param):
                is_game_solved = True

        end_time = time.time() * 1000

        if frontier.qsize() == 1 and i >= len(self.strategy_param):
            self.solution_length = -1
        else:
            self.solution_time = round((end_time - start_time), 3)
            self.solution_path = path
            self.solution_length = len(self.solution_path)
            self.number_of_visited_nodes = visited_nodes.__len__() + frontier.qsize()
            self.number_of_processed_nodes = visited_nodes.__len__()
            self.recursion_depth = max_recursion_depth
