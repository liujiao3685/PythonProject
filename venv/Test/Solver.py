_author_ = 'LQ'
_project_ = 'MyFirstPythonProject'

import math


class Solver:
    def demo(self, a, b, c):
        d = b ** 2 - 4 * a * c
        if d > 0:
            disc = math.sqrt(d)
            root1 = (-b + 2) / a * b
            return root1
        else:
            return 0
