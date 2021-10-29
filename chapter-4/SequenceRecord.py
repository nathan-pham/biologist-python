class SequenceRecord:
    
    def __init__(self, sequence="ACGTAGCTGACGATC", gene_name="ABC1", species_name="Drosophila melanogaster"):
        self.sequence = sequence
        self.gene_name = gene_name
        self.species_name = species_name

    @property
    def fasta(self):
        return "> " + self.gene_name + "_" + self.species_name.replace(" ", "_") + "\n" + self.sequence