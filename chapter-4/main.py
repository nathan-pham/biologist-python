from ProteinRecord import ProteinRecord
from DNARecord import DNARecord

dna = DNARecord(
    sequence="ACGTAGCTGACGATC",
    gene_name="ABC1",
    species_name="Drosophila melanogaster",
    genetic_code=5
)

protein = ProteinRecord(
    sequence="ACGTAGCTGACGATC",
    gene_name="ABC1",
    species_name="Drosophila melanogaster"
)

print(f"genetic code: {dna.genetic_code}")
print(f"complement: {dna.complement()}")
print(f"protein: {dna.translate()}")
print(f"{dna.get_AT():.2f}")
print(dna.fasta)

print(f"protein hydrophobic: {protein.hydrophobic:.2f}")