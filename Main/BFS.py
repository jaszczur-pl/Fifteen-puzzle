#!/usr/bin/env python3
# 15-puzzle game solver with BFS(breadth-first search) algorithm

from random import shuffle
from queue import PriorityQueue


class Puzzle:

    def create_and_fill_queue(self):
        myQueue = PriorityQueue()

        while not myQueue.empty():
            print(myQueue.get())
