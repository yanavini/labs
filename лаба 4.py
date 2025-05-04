#лаба 4 задание 1 вариант 3
from Bio import SeqIO

file1 = "C:/Users/1995b/Downloads/sequence(1).gb"
file2 = "C:/Users/1995b/Downloads/sequence(2).gb"
output_file = "combined_species.gb"

with open(output_file, "wb") as outfile:
    for record in SeqIO.parse(file1, "genbank"):
        SeqIO.write(record, outfile, "genbank")

    for record in SeqIO.parse(file2, "genbank"):
        SeqIO.write(record, outfile, "genbank")

print(f"Файлы объединены в {output_file}!")
лаба 4 задание 2 вариант 3
def calculate_gc_content(sequence):

    g_count = sequence.count('G')
    c_count = sequence.count('C')
    total_count = len(sequence)
    if total_count == 0:
        return 0
    return (g_count + c_count) / total_count * 100

def main(input_file):
    records_gc = []

    for record in SeqIO.parse(input_file, "genbank"):
        gc_content = calculate_gc_content(str(record.seq))
        records_gc.append((record, gc_content))

    records_gc.sort(key=lambda x: x[1])

    for record, gc_content in records_gc:
        print(f"ID: {record.id}, GC Content: {gc_content:.2f}%, Sequence: {record.seq}")

if __name__ == "__main__":
    input_file = "C:/Users/vlada/PycharmProjects/pythonProject1/.venv/Scripts/combined_species.gb"