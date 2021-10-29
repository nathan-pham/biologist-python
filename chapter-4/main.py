from ProteinRecord import ProteinRecord
from DNARecord import DNARecord

dna = DNARecord()
print(f"complement: {dna.complement()}")
print(f"protein: {dna.translate()}")
print(f"{dna.get_AT():.2f}")
print(dna.fasta)