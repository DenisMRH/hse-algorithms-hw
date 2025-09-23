from typing import Iterable, List


def max_even_sum(nums: Iterable[int]) -> int:
    total = 0
    min_odd = None

    for x in nums:
        total += x
        if x & 1:
            if min_odd is None or x < min_odd:
                min_odd = x

    if total % 2 == 0:
        return total
    if min_odd is None:
        return 0
    return total - min_odd


def _parse_input(line: str) -> List[int]:
    line = (line).strip()
    if not line:
        return []
    parts = line.split()
    nums: List[int] = []
    for p in parts:
        try:
            v = int(p)
        except ValueError as e:
            raise ValueError(f"Невозможно распознать число: {p}")
        if v < 0:
            raise ValueError(f"Ожидались неотрицательные числа, встретилось: {v}")
        nums.append(v)
    return nums


def main() -> None:
    import sys
    if sys.stdin.isatty():
        data = input().strip()
    else:
        data = sys.stdin.read()
    nums = _parse_input(data)
    print(max_even_sum(nums))


if __name__ == "__main__":
    main()