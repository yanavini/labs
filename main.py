
import itertools
# Вариант 4
def kek (n):
    numbers = list(range(1, n + 1))
    permutations = list(itertools.permutations(numbers))
    return permutations

def main():
    n = int(input("Введите натуральное число n (<= 7): "))
    permutations = kek (n)
    print(f"Общее число перестановок длины {n}: {len(permutations)}")
    print("Список всех перестановок:")
    for perm in permutations:
        print(perm)
if __name__ == "__main__":
    main()
