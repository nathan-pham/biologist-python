import re

class SequenceRecord:
    
    def __init__(self, sequence, gene_name, species_name):
        if not re.match(r"[A-Z][a-z]+ [a-z]+", species_name): 
            exit(f"{species_name} is not a valid species name")

        self.sequence = sequence
        self.gene_name = gene_name
        self.species_name = species_name

    @property
    def fasta(self):
        return "> " + self.gene_name + "_" + self.species_name.replace(" ", "_") + "\n" + self.sequence