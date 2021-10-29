from SequenceRecord import SequenceRecord

class ProteinRecord(SequenceRecord):

    @property
    def hydrophobic(self):
        amino_acids = ['A','I','L','M','F','W','Y','V']
        total = 0

        for a in amino_acids:
            total += self.sequence.count(a.upper())

        return (total / len(self.sequence)) * 100