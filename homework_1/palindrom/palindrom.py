def is_palindrom(x: str) -> bool:
    if x.strip().isdigit():
        x = int(x.strip())
        original = x
        reversed_num = 0
        if x < 0:
            print("Число отрицательное")
            return False

        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        print("True" if original == reversed_num else "False")
        return(True if original == reversed_num else False)
    else:
        print("Это не целое положительное число, приятель")
        return False


if __name__ == "__main__":
    x = input('Введи целое положительное число: ')
    is_palindrom(x)
