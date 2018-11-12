#!/usr/bin/env python3
import sys

sys.path.insert(0, '../')
from Main.BFS import BFS
from Main.DFS import DFS
from Main.IOHandler import IOHandler


def main():
    io_handler = IOHandler()
    input_values = io_handler.read_input_file()
    strategy = io_handler.get_strategy
    strategy_param = io_handler.get_strategy_param

    if strategy == 'bfs':
        bfs = BFS(strategy_param, input_values)
        bfs.solve_puzzle()

        io_handler.write_result_file(bfs.solution_length, bfs.solution_path)
        io_handler.write_stat_file(bfs.solution_length, bfs.number_of_visited_nodes, bfs.number_of_processed_nodes, \
                                   bfs.recursion_depth, bfs.solution_time)
    elif strategy == 'dfs':
        dfs = DFS(strategy_param, input_values)
        dfs.solve_puzzle()

        if dfs.solution_length == -1:
            io_handler.write_wrong_result_file(dfs.solution_length)
            io_handler.write_wrong_stat_file(dfs.solution_length)
        else:
            io_handler.write_result_file(dfs.solution_length, dfs.solution_path)
            io_handler.write_stat_file(dfs.solution_length, dfs.number_of_visited_nodes, dfs.number_of_processed_nodes,\
                                       dfs.recursion_depth, dfs.solution_time)
    elif strategy == 'astr':
        print('astr')
    else:
        print('nieprawdiłowa nazwa strategii')


if __name__ == '__main__':
    main()
