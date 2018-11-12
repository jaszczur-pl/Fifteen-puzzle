
class StrategiesParent:
    solution_length = None
    solution_path = ''

    number_of_visited_nodes = None
    number_of_processed_nodes = None
    recursion_depth = 0
    solution_time = None

    def __init__(self, strategy_param, input_values):
        self.strategy_param = strategy_param  # for BFS and DFS it is the random queue of characters 'l' 'r' 'u' 'd'
        # for A* it is one of the heuristics (manh - Manhattan or hamm - Hamming)
        self.matrix_length = input_values[0]
        self.matrix_height = input_values[1]
        self.puzzle = input_values[2:]

    def visit_node(self, node, sorted_puzzle):
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
        full_value, rest_value = divmod(zero_index, self.matrix_length)  # Divide the 0 field index by the array length

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
