
from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    buckets: dict[tuple[str, ...], list[str]] = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        buckets[key].append(s)

    groups = [sorted(words) for words in buckets.values()]
    groups.sort(key=lambda g: (len(g), g[0] if g else ""))
    return groups


if __name__ == "__main__":
    arrstr = input("Введите элементы массива через пробел: ").split()
    print(group_anagrams(arrstr))
