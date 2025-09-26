from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence


def add(a: int | float, b: int | float) -> float:
    """두 수를 더해 float 로 반환."""
    return float(a + b)


def factorial(n: int) -> int:
    """n! (n >= 0). 음수이면 ValueError.

    반복(iterative) 방식 → 재귀보다 스택 안전.
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


@dataclass(slots=True)
class Stats:
    """간단한 통계 계산용.

    values: 숫자 시퀀스
    mean(): 산술 평균 (비어있으면 0.0)
    variance(): 표본이 2개 미만이면 0.0, 모집단 분산 (n) 기준
    """

    values: Sequence[float]

    def _iter(self) -> Iterable[float]:
        return (float(v) for v in self.values)

    def mean(self) -> float:
        total = 0.0
        count = 0
        for v in self._iter():
            total += v
            count += 1
        return total / count if count else 0.0

    def variance(self) -> float:
        vals = list(self._iter())
        n = len(vals)
        if n < 2:
            return 0.0
        m = sum(vals) / n
        return sum((x - m) ** 2 for x in vals) / n
