from random import randint


def generate_kmers(length):
    bases = ['A', 'T', 'G', 'C']
    result = ['']

    for i in range(length):
        new_result = []

        for kmer in result:
            for base in bases:
                new_result.append(kmer + base)

        result = new_result

    return result

def generate_kmers_recursively(length):
    bases = ['A', 'T', 'G', 'C']

    if length == 1:
        return bases
    else:
        result = []

        for sequence in generate_kmers_recursively(length - 1):
            for base in bases:
                result.append(sequence + base)

        return result

# imperative method
print(generate_kmers(3))

# recursive method
print(generate_kmers_recursively(3))