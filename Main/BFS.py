# BFS(breadth-first search) algorithm for 15-puzzle game solver

from queue import Queue
import time


class BFS:

    solution_length = None
    solution_path = ''

    number_of_visited_nodes = None
    number_of_processed_nodes = None
    recursion_depth = None
    solution_time = None

    def __init__(self, strategy_param, input_values):
        self.strategy_param = strategy_param  # for BFS it is the random queue of characters 'l' 'r' 'u' 'd'
        self.matrix_length = input_values[0]
        self.matrix_height = input_values[1]
        self.puzzle = input_values[2:]

    def solve_puzzle(self):
        global sorted_puzzle, current_node

        number_of_puzzle_elements = len(self.puzzle)
        frontier = Queue()
        path = Queue()
        frontier.put(self.puzzle)
        visited_nodes = []
        is_game_solved = False
        sorted_puzzle = self.sort_puzzle(number_of_puzzle_elements)

        start_time = time.time() * 1000

        while not is_game_solved:
            current_node = frontier.get()
            is_game_solved = self.visit_node(current_node)
            visited_nodes.append(current_node)

            if is_game_solved:
                break

            for move_type in self.strategy_param:
                next_node = self.check_possible_moves(move_type, current_node[:])
                if next_node is not None and next_node not in visited_nodes:
                    frontier.put(next_node)
                    path.put(self.solution_path + move_type)

            self.solution_path = path.get()

        end_time = time.time() * 1000

        self.solution_time = round((end_time - start_time), 3)
        self.solution_length = len(self.solution_path)
        self.number_of_visited_nodes = visited_nodes.__len__()
        self.number_of_processed_nodes = self.number_of_visited_nodes + frontier.qsize()
        self.recursion_depth = len(self.solution_path)

        print('game solved!' + str(current_node) + ' ' + str(self.solution_time))
        print(self.number_of_visited_nodes)
        print(self.number_of_processed_nodes)
        print(self.solution_path)
        print(self.solution_length)


    def visit_node(self, node):
        if node == sorted_puzzle:
            return True
        else:
            return False

    def sort_puzzle(self, number_of_elements):
        sorted_values = []
        for i in range(1, number_of_elements):
            sorted_values.append(i)

        sorted_values.append(0)
        return sorted_values

    def check_possible_moves(self, move_type, puzzle):

        zero_index = puzzle.index(0)
        full_value, rest_value = divmod(zero_index, self.matrix_length)  # Divide the zero index by the array length

        if (move_type == 'L' or move_type == 'l') and rest_value != 0:
            puzzle[zero_index], puzzle[zero_index - 1] = puzzle[zero_index - 1], puzzle[zero_index]  # swap numbers

            return puzzle

        if (move_type == 'R' or move_type == 'r') and rest_value != (self.matrix_length - 1):
            puzzle[zero_index], puzzle[zero_index + 1] = puzzle[zero_index + 1], puzzle[zero_index]  # swap numbers

            return puzzle

        if (move_type == 'U' or move_type == 'u') and full_value != 0:
            puzzle[zero_index], puzzle[zero_index - self.matrix_length] = puzzle[zero_index - self.matrix_length], \
                                                                          puzzle[zero_index]  # swap numbers

            return puzzle

        if (move_type == 'D' or move_type == 'd') and full_value != (self.matrix_height - 1):
            puzzle[zero_index], puzzle[zero_index + self.matrix_length] = puzzle[zero_index + self.matrix_length], \
                                                                          puzzle[zero_index]  # swap numbers

            return puzzle
