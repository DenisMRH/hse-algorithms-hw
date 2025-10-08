def two_sum (arr :str, k: str):
    arr = (arr.strip()).split()
    print(arr)
    print(k)

if __name__ == "__main__":
    arr = input("Напиши элименты массива через пробел: ")
    k = input("Напиши сумму двух элементов, которую ты ищешь: ")
    two_sum(arr,k)
