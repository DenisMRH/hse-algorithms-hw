def two_sum(arrstr : list, k: str):
    if len(arrstr)<2:
        raise ValueError("В массиве менее двух элементов")

    arr = []
    
    for x in arrstr:
        if not (x.lstrip("-").isdigit()):
            raise ValueError(f"Ожидалось число, пришло: {x}")
        arr.append(int(x))

    seen = {}  
    for i, num in enumerate(arr):
        target = k - num
        if target in seen:
            return tuple(sorted((seen[target], i)))
        seen[num] = i
    raise ValueError("Пара не найдена")  

if __name__ == "__main__":
    arrstr = input("Введите элементы массива через пробел: ").split()
    k = input("Введите k: ")
    
    if not (k.lstrip("-")).isdigit():
        raise ValueError(f"Ожидалось число, пришло: {k}")
    k=int(k)

    i, j = two_sum(arrstr, k)
    print(i, j)
