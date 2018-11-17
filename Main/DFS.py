# DFS(depth-first search) algorithm for 15-puzzle game solver

from queue import LifoQueue
import time
from Main.StrategiesParent import StrategiesParent


class DFS(StrategiesParent):

    def __init__(self, strategy_param, input_values):
        super().__init__(strategy_param, input_values)
        self.max_recursion_depth = 6

    def solve_puzzle(self):

        global current_node
        current_node = tuple(self.puzzle)
        number_of_puzzle_elements = len(self.puzzle)
        frontier = LifoQueue(maxsize=self.max_recursion_depth + 1)
        frontier.put(tuple(self.puzzle))
        path = ''
        visited_nodes = [tuple(self.puzzle)]
        is_game_solved = False
        sorted_puzzle = self.sort_puzzle(number_of_puzzle_elements)

        start_time = time.time() * 1000

        is_game_solved = self.visit_node(self.puzzle, sorted_puzzle)

        i = 0
        while not is_game_solved:

            if i >= len(self.strategy_param) or frontier.full():
                frontier.get()
                path = path[:-1]
                i = 0
                current_node = frontier.get()
                frontier.put(current_node)

            next_node = self.check_possible_moves(self.strategy_param[i], list(current_node[:]))

            if next_node is None or next_node in visited_nodes:
                i += 1
            else:
                path += self.strategy_param[i]
                i = 0
                current_node = next_node
                frontier.put(current_node)
                is_game_solved = self.visit_node(current_node, sorted_puzzle)
                visited_nodes.append(current_node)

            if frontier.qsize() == 1 and i >= len(self.strategy_param):
                # print(frontier.get())
                # print(i)
                break

        end_time = time.time() * 1000

        if frontier.qsize() == 1 and i >= len(self.strategy_param):
            self.solution_length = -1
        else:
            self.solution_time = round((end_time - start_time), 3)
            self.solution_path = path
            self.solution_length = len(self.solution_path)
            self.number_of_visited_nodes = visited_nodes.__len__()
            self.number_of_processed_nodes = frontier.qsize()
            self.recursion_depth = (frontier.qsize() - 1)
