import collections
import copy
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

# 12:00 - 12:20

from collections import defaultdict
from collections import deque
import copy

def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:
    # TODO - you fill in here.
    # build graph
    graph = defaultdict(list)
    jmax = len(maze) - 1
    imax = len(maze[0]) - 1
    for j in range(len(maze)):
        for i in range(len(maze[0])):
            if maze[j][i] == WHITE:
                point = Coordinate(j, i)
                i2, j2 = i-1, j
                if i2 >= 0 and maze[j2][i2] == WHITE:
                    point2 = Coordinate(j2, i2)
                    graph[point].append(point2)
                i2, j2 = i+1, j
                if i2 <= imax and maze[j2][i2] == WHITE:
                    point2 = Coordinate(j2, i2)
                    graph[point].append(point2)
                i2, j2 = i, j - 1
                if j2 >= 0 and maze[j2][i2] == WHITE:
                    point2 = Coordinate(j2, i2)
                    graph[point].append(point2)
                i2, j2 = i, j + 1
                if j2 <= jmax and maze[j2][i2] == WHITE:
                    point2 = Coordinate(j2, i2)
                    graph[point].append(point2)
    visited = set()
    queue = deque([[s]])
    solution = []
    while not solution and queue:
        path = queue.popleft()
        node = path[-1]
        visited.add(node)
        for neighbor in graph[node]:
            if not neighbor in visited:
                if neighbor == e:
                    solution = path
                    solution.append(neighbor)
                    break
                else:
                    new_path = path.copy()
                    new_path.append(neighbor)
                    queue.append(new_path)
    return solution

def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))
