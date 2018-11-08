#!/usr/bin/env python3
import sys
sys.path.insert(0, '../')
from Main.BFS import BFS
from Main.IOHandler import IOHandler


def main():
    io_handler = IOHandler()
    input_values = io_handler.read_input_file()
    strategy = io_handler.get_strategy
    strategy_param = io_handler.get_strategy_param

    if strategy == 'bfs':
        bfs = BFS(strategy_param, input_values)
        bfs.solve_puzzle()
    elif strategy == 'dfs':
        print('dfs')
    elif strategy == 'astr':
        print('astr')
    else:
        print('nieprawdiłowa nazwa strategii')

    # io_handler.write_result_file(5, 'LDUR')
    # io_handler.write_stat_file(5, 13, 5, 5, 3.453)


if __name__ == '__main__':
    main()
