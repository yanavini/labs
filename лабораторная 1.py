#Вариант 7

def long(sequences):
    def common(substring, sequences):
        return all(substring in seq for seq in sequences)

    def longest(sequences):
        if not sequences:
            return ""

        reference = sequences[0]
        ref_len = len(reference)
        substring = ""

        for i in range(ref_len):
            for j in range(i + 1, ref_len + 1):
                candidate = reference[i:j]
                if common(candidate, sequences) and len(candidate) > len(substring):
                    substring = candidate

        return substring

    sequences = [seq.strip() for seq in sequences if seq.strip()]
    return longest(sequences)


def get():
    sequences = []
    print("Введите последовательности ДНК (пустая строка для завершения ввода):")
    while True:
        seq = input("Введите последовательность: ").strip().upper()
        if not seq:
            break
        sequences.append(seq)

    return sequences


if __name__ == "__main__":
    sequences = get()
    if sequences:
        result = long(sequences)
        print(f"Самая длинная общая подстрока: {result}")
    else:
        print("Не введено ни одной последовательности.")

