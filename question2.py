from operator import xor


def output(value: int):
    def multiple_of_3(x): return x % 3 == 0
    def multiple_of_5(x): return x % 5 == 0

    count = 0

    for i in range(1, value + 1):
        if not xor(multiple_of_3(i), multiple_of_5(i)):
            count += 1

    return count


value = int(input("Value: "))
print(output(value))
