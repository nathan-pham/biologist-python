from random import randint

bases = ['A', 'T', 'G', 'C']

def generate_kmers(length):
    result = []
    for i in range(length):
        result.append(bases[randint(0, len(bases) - 1)])
    return result

print(generate_kmers(3))