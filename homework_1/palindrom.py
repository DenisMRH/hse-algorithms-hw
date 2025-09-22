def is_palindrom(x: int) -> bool:
    if x < 0:
        return False

    original = x
    reversed_num = 0

    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10

    return original == reversed_num


if __name__ == "__main__":
    x = input('Введи число: ').strip()
    if x.isdigit():
        print("True" if is_palindrom(int(x)) else "False")
    else:
        print("Это не число, приятель")
