import math
from typing import List


class ArgumentException(Exception):
    pass


class Solver:
    """Класс решения квадратного уравнения."""
    def _calculate_discriminant(self, a: float, b: float, c: float) -> float:
        """Метод нахождения дискриминанта"""
        return b**2 - 4 * a * c

    def _calculate_roots(self, D: float, a: float, b: float) -> float:
        """Метод вычисления корней квадратного уравнения"""
        _sqrtD = math.sqrt(D)
        root1 = (-b + _sqrtD) / (2 * a)
        root2 = (-b - _sqrtD) / (2 * a)

        return [root1, root2]

    def solve(self, a: float, b: float, c: float, eps: float = 1e-5) -> List[float]:
        """Решение квадратного уравнения вида ax^2 + bx + c = 0"""
        if any([not (isinstance(n, float) or isinstance(n, int)) for n in (a, b, c)]):
            raise ArgumentException('переданные аргументы не являются числом')

        D = self._calculate_discriminant(a, b, c)

        if abs(a) < eps:
            raise ArgumentException('a не равно 0')

        if D < 0:
            return []

        if abs(D) < eps:
            root1, root2 = self._calculate_roots(0, a, b)
            return [root1, root2]

        root1, root2 = self._calculate_roots(D, a, b)
        return [root1, root2]
