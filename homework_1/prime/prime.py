def count_prime (number: str) -> int:
    try:
        number = int(number.strip())
    except ValueError:
        raise ValueError(f"Ожидали целое число, получили: {number}")
    if number<=0:
        return 0
    
    count_primes=0

    for i in range(2,number):
        for j in range(2,i+1):
            if j!=i:
                if i % j == 0:
                    break
            else:
                count_primes+=1
    return count_primes



if __name__ == "__main__":
    number = input("Введите число: ")
    print(count_prime(number))