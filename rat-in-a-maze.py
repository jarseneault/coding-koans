import unittest

BLOCKED = 0
ROOM = 1
VISITED = 2

POSSIBLE_DIRECTIONS = {
    'D': (0, 1),
    'R': (1, 0),
    'U': (0, -1),
    'L': (-1, 0)
}


def findPath(arr, n):
    solutions = []
    findPathHelper(arr, n, 0, 0, '', solutions)
    solutions.sort()
    return ' '.join(solutions)


def findPathHelper(arr, n, x=0, y=0, path='', solutions=None):
    target_x = n - 1
    target_y = n - 1
    arr[y][x] = VISITED
    if x == target_x and y == target_y:
        solutions.append(path)
        arr[y][x] = ROOM
        return
    original_path = path
    for ordinal_direction, delta in POSSIBLE_DIRECTIONS.items():
        path = path + ordinal_direction
        delta_x = delta[0]
        delta_y = delta[1]
        modified_x = x + delta_x
        modified_y = y + delta_y
        if isSafe(arr, modified_x, modified_y, n):
            findPathHelper(arr, n, modified_x, modified_y, path, solutions)
        path = original_path
    arr[y][x] = ROOM


def isSafe(arr, x, y, n):
    return 0 <= x < n and 0 <= y < n and arr[y][x] == ROOM


class Tests(unittest.TestCase):
    def test_find_path(self):
        problem_sets = [
            ([[1, 0, 0],
              [1, 1, 1],
              [1, 1, 1]], 'DDRR DDRURD DRDR DRRD'),
            ([[0]], ''),
            ([[1]], ''),
            ([[0, 0],
              [0, 0]], ''),
            ([[1, 0, 1, 1, 1],
              [1, 0, 1, 0, 1],
              [1, 0, 1, 1, 1],
              [1, 0, 1, 0, 1],
              [1, 1, 1, 0, 1]], 'DDDDRRUURRDD DDDDRRUUUURRDDDD')
        ]
        for problem_set in problem_sets:
            self.assertEqual(problem_set[1], findPath(problem_set[0], len(problem_set[0][0])))


if __name__ == "__main__":
    unittest.main()
