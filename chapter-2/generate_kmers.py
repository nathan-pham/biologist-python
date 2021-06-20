from random import randint

def generate_kmers(length):
    bases = ['A', 'T', 'G', 'C']
    result = ['']

    # repeat for the length of kmers
    for i in range(length):
        new_result = []

        # loop through existing results & add a base to it
        for kmer in result:
            for base in bases:
                new_result.append(kmer + base)

        # set result to new result
        result = new_result

    return result

def generate_kmers_recursively(length):
    bases = ['A', 'T', 'G', 'C']

    # if length is 1 then return default bases
    if length == 1:
        return bases
    else:
        result = []

        # create a sequence one less than the length & add all of the bases to it
        for sequence in generate_kmers_recursively(length - 1):
            for base in bases:
                result.append(sequence + base)

        return result

# imperative method
print(generate_kmers(3))

# recursive method
print(generate_kmers_recursively(3))