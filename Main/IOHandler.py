import sys


class IOHandler:

    def __init__(self):
        self.strategy = sys.argv[1]
        self.strategy_param = sys.argv[2]

        if sys.argv.__len__() < 4:
            self.input_file_name = 'a.txt'
        else:
            self.input_file_name = sys.argv[3]

        if sys.argv.__len__() < 5:
            self.output_result_file_name = 'b.txt'
        else:
            self.output_result_file_name = sys.argv[4]

        if sys.argv.__len__() < 6:
            self.output_stat_file_name = 'c.txt'
        else:
            self.output_stat_file_name = sys.argv[5]

    @property
    def get_strategy(self):
        return self.strategy

    @property
    def get_strategy_param(self):
        return self.strategy_param

    def read_input_file(self):
        input_file = open(self.input_file_name)
        array = []
        lines = input_file.read().splitlines()
        cnt = 0

        for line in lines:
            line = lines[cnt].split()
            for field in line:
                array.append(field)
            cnt += 1

        input_file.close()

        tuple_int = tuple(map(int, array))

        return tuple_int

    def write_result_file(self, move_counter, move_sequence):
        output_file = open(self.output_result_file_name, 'w')
        output_file.write(str(move_counter) + "\n" + move_sequence)
        output_file.close()

    def write_wrong_result_file(self, move_counter):
        output_file = open(self.output_result_file_name, 'w')
        output_file.write(str(move_counter))
        output_file.close()

    def write_stat_file(self, move_counter, number_of_visited_states, number_of_processed_states, max_recursion_depth,
                        processing_time):

        output_file = open(self.output_stat_file_name, 'w')
        output_file.write(str(move_counter) + "\n" + str(number_of_visited_states) + "\n" \
                          + str(number_of_processed_states) + "\n" + str(max_recursion_depth) + "\n" \
                          + str(processing_time))
        output_file.close()

    def write_wrong_stat_file(self, move_counter):

        output_file = open(self.output_stat_file_name, 'w')
        output_file.write(str(move_counter))
        output_file.close()
