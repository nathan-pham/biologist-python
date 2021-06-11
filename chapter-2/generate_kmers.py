from random import randint


def generate_kmers(length):
    bases = ['A', 'T', 'G', 'C']
    result = ['']

    for i in range(length):
        for j in range(len(result)):
            for base in bases:
                result[j] += base

    return result

print(generate_kmers(3))