from SequenceRecord import SequenceRecord 

class DNARecord(SequenceRecord):

    def __init__(self, sequence, gene_name, species_name, genetic_code):
        self.sequence = sequence
        self.gene_name = gene_name
        self.species_name = species_name
        self.genetic_code = genetic_code


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
