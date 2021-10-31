# custom iterable types
class DNASequence:
    sequence = 'atgccgcat' 
    _position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._position < len(self.sequence) - 2:
            codon = self.sequence[self._position:self._position + 3]
            self._position += 3
            return codon
        else:
            raise StopIteration

sequence = DNASequence()
for base in sequence:
    print(base)


# ============================================================ #


# custom generators (uses yield to return one result at a time)
def get_4mers(dna):
    offset = 4

    for i in range(0, len(dna) - offset + 1):
        yield dna[i:i + offset]

for x in get_4mers('actggcgtgcatg'):
    print(x)