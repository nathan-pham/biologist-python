# tuples are immutable lists
ex_tuple = ('Nathan Pham', 'California', 16)


# ============================================================ #


# sets limit repetition, stores individual values
# hardcoded set: processed = { 1, 2, 3 }
accessions = ['ok', 'ok', 'ok', 'bruh']
processed = set()

for acc in accessions: 
    if not acc in processed:
        processed.add(acc)
    
print(processed)


# ============================================================ #


# multidimensional list
alignments = [['A', 'T', '-', 'T', 'G'], 
              ['A', 'A', 'T', 'A', 'G'], 
              ['T', '-', 'T', 'T', 'G'], 
              ['A', 'A', '-', 'T', 'A']] 

# select a row
sequence = alignments[0]
print(sequence)

# select an item within a row
character = sequence[2] # sequence[0][2]
print(character)

# select a column
column = [row[0] for row in alignments]
print(column)


# ============================================================ #


# dict of sets
gene_sets = {
    'arsenic' : { 1, 2, 3, 4, 5, 6, 8, 12 },
    'cadmium' : { 2, 12, 6, 4 },
    'copper'  : { 7, 6, 10, 4, 8 },
    'mercury' : { 3, 2, 4, 5, 1 }
}

# is gene 3 expressed in response to cadium?
print(3 in gene_sets['cadmium'])

# what conditions are gene 4 expressed in?
for (metal, genes) in gene_sets.items():
    if 4 in genes:
        print(metal)

# more concisely using list comprehension
print([ metal for (metal, genes) in gene_sets.items() if 4 in genes ])

# determine gene subsets
for (metalA, listA) in gene_sets.items():
    for (metalB, listB) in gene_sets.items():
        if(listA.issubset(listB) and metalB != metalA):
            print(f'{ metalA } is a subset of { metalB }')


# ============================================================ #


# dicts of tuples
records = {
    'ABC123' : ('actgctagt', 1),
    'XYZ456' : ('ttaggttta', 1),
    'HIJ789' : ('cgcgatcgt', 5)
}

# retrieve a record
(sequence, code) = records.get('HIJ789')
print(f'sequence: { sequence } code: { code }')


# ============================================================ #


# track frequency of kmers
dna = 'aattggaattggaattg'
count = {}
k = 4

for i in range(len(dna) - k + 1):
    kmer = dna[i:i + k]
    count[kmer] = count.get(kmer, 0) + 1

print(count)

# retrieve position at which a kmer occurs
position = {}

for i in range(len(dna) - k + 1):
    kmer = dna[i:i + k]
    array = position.get(kmer, [])
    array.append(i)
    position[kmer] = array

print(position)