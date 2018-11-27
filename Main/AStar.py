# A*(A star) algorithm for 15-puzzle game solver. Algorithm can use both Manhattan and Hamming heuristics.

from queue import PriorityQueue
import time
from StrategiesParent import StrategiesParent


class AStar(StrategiesParent):

    def solve_puzzle(self):

        number_of_puzzle_elements = len(self.puzzle)
        frontier = PriorityQueue()

        move_type = ''
        frontier.put((0, [self.puzzle, None, move_type]))
        visited_nodes = {}
        sorted_puzzle = self.sort_puzzle(number_of_puzzle_elements)
        g_score = {self.puzzle: 0}
        is_game_solved = False

        start_time = time.time() * 1000

        while not is_game_solved:
            node_list = frontier.get()[1]

            current_node = node_list[0]
            next_node = node_list[1]
            move_type = node_list[2]

            is_game_solved = self.visit_node(current_node, sorted_puzzle)
            visited_nodes[current_node] = (next_node, move_type)

            if is_game_solved:
                break

            for move_type in 'uldr':
                next_node = self.check_possible_moves(move_type, list(current_node[:]))

                if next_node is not None and next_node not in visited_nodes:
                    temp_g_score = g_score[current_node] + 1
                    h_score = self.calc_heuristic_value(next_node, sorted_puzzle)

                    g_score[next_node] = temp_g_score
                    priority = temp_g_score + h_score
                    frontier.put((priority, [next_node, current_node, move_type]))

        path = self.find_path(visited_nodes, self.puzzle, sorted_puzzle)
        end_time = time.time() * 1000

        self.solution_path = path
        self.solution_time = round((end_time - start_time), 3)
        self.solution_length = len(self.solution_path)
        self.number_of_visited_nodes = visited_nodes.__len__() + frontier.qsize()
        self.number_of_processed_nodes = visited_nodes.__len__()
        self.recursion_depth = len(self.solution_path)

    # calculate heuristic value(h score) depending on the given strategy parameter (Hamming or Manhattan)
    def calc_heuristic_value(self, node, final_puzzle):
        heuristic_value = 0

        if self.strategy_param == 'hamm':  # Hamming distance
            for i in range(len(node)-1):
                if node[i] != final_puzzle[i]:
                    heuristic_value += 1

        if self.strategy_param == 'manh':  # Manhattan distance
            for i, j in enumerate(node):
                if node[i] != 0:
                    node_x, node_y = int(i / self.matrix_height), int(i % self.matrix_length)
                    final_x, final_y = int((j - 1) / self.matrix_height), int(j - 1) % self.matrix_length
                    heuristic_value += abs(node_x - final_x) + abs(node_y - final_y)

        return heuristic_value

    def find_path(self, came_from_dict, start_node, end_node):
        current_node = end_node
        temp_path = ''
        while current_node != start_node:
            prev_tuple = came_from_dict.get(current_node)
            prev_node = prev_tuple[0]
            prev_move = prev_tuple[1]

            temp_path += prev_move
            current_node = prev_node

        temp_path = temp_path[::-1]  # reverse string
        return temp_path


