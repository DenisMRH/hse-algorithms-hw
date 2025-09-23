def max_even_sum(line: str) -> int:
    line = (line).strip()
    if not line:
        return 0
    parts = line.split()
    nums = []
    for p in parts:
        try:
            v = int(p)
        except ValueError as e:
            raise ValueError(f"Ожидались целые числа, встретилось: {p}")
        if v < 0:
            raise ValueError(f"Ожидались неотрицательные числа, встретилось: {v}")
        nums.append(v)
    
    total = 0
    min_odd = None

    for x in nums:
        total += x
        if (x % 2 != 0) and (min_odd is None or x < min_odd):
            min_odd = x

    if total % 2 == 0:
        return total
    if min_odd is None:
        return 0
    return total - min_odd


if __name__ == "__main__":
    data = input("Введите целые положительные числа через пробел: ")
    print(max_even_sum(data))
