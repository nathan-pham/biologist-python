from SequenceRecord import SequenceRecord 

class DNARecord(SequenceRecord):
        
    def complement(self):
        return (self.sequence.replace("A", "t")
                            .replace("T", "a")
                            .replace("C", "g")
                            .replace("G", "c")
                            .upper())
    
    def get_AT(self):
        return (self.sequence.count("A") + self.sequence.count("T")) / len(self.sequence)


    def translate(self):
        gene_code = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
        
        protein = ""

        for i in range(0, len(self.sequence) - 2, 3):
            codon = self.sequence[i:i + 3]
            protein += gene_code.get(codon.upper(), "X")

        return protein

class ProteinRecord(DNARecord):
    def __init__(self, sequence="ACGTAGCTGACGATC", gene_name="ABC1", species_name="Drosophila melanogaster"):
        self.sequence = sequence
        self.gene_name = gene_name
        self.species_name = species_name

    @property
    def hydrophobic(self):
        amino_acids = ['A','I','L','M','F','W','Y','V']
        total = 0

        for a in amino_acids:
            total += self.sequence.count(a.upper())

        return (total / len(self.sequence)) * 100

dna = DNARecord()
print(f"complement: {dna.complement()}")
print(f"protein: {dna.translate()}")
print(f"{dna.get_AT():.2f}")
print(dna)