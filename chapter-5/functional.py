import re

# lambda anonymous functions
def print_with_function(arr, function):
    for i in arr:
        print(function(i))

print_with_function(["Hello", "World", "Bruh"], lambda input : input[1])


# ============================================================ #


# declarative programmming style
print(sum(range(11)))


# ============================================================ #


dna_list = ['TAGC', 'ACGTATGC', 'ATG', 'ACGGCTAG']

# higher order function: map
lengths = list(map(lambda v : len(v), dna_list))
at_contents = list(map(lambda v : (v.count("A") + v.count("T") / len(v)), dna_list))
print(f"lengths: {lengths}")
print(f"AT: {at_contents}")


# ============================================================ #


# higher order function: filter
big_dna = list(filter(lambda v : len(v) > 5, dna_list))
small_at = list(filter(lambda v : v < 0.6, at_contents))
print(f"DNA longer than 5: {big_dna}")
print(f"AT less than 0.6: {small_at}")


# ============================================================ #


# higher order function: sorted (stable)
sorted_dna = sorted(dna_list, key=lambda v : len(v), reverse=False)
print(f"sorted DNA: {sorted_dna}")

dna_list = ['ATCGA', 'ACGG', 'CGTAAA', 'ATCGAA'] 

def poly_a_length(dna):
    matches = re.search(r'A+$', dna)
    return len(matches.group()) if matches else 0

sorted_by_poly_a = sorted(dna_list, key=poly_a_length)
print(f"sorted DNA by poly a tail: {sorted_by_poly_a}")

# ============================================================ #


# double sorting
loci = [ 
    # locus, base position, gene name
    (4, 9200, 'gene1'), 
    (6, 63788, 'gene2'), 
    (4, 7633, 'gene3'), 
    (2, 8766, 'gene4') 
]

sorted_by_locus = sorted(loci, key=lambda v : v[0])
sorted_by_base = sorted(sorted_by_locus, key=lambda v : v[1])
print(f"sorted by locus -> base: {sorted_by_base}")