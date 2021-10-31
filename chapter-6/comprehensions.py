# list comprehensions, often more readable than map
dna_list = ['TAGC', 'ACGTATGC', 'ATG', 'ACGGCTAG'] 
lengths = [len(dna) for dna in dna_list if dna.startswith("A")]
print(f"lengths: {lengths}")


# ============================================================ #


# exhaustable generators to achieve faster speed
generator = (2 ** x for x in range(1000))


# ============================================================ #


# nested list comprehensions
bases = ['A', 'C', 'G', 'T']
dna_pairs = [b1 + b2 for b1 in bases for b2 in bases if b1 != b2]
print(f"unique DNA pairs: {dna_pairs}")


# ============================================================ #


# dictionary comprehensions
dna_dict = {dna: len(dna) for dna in dna_list}
print(f"DNA dict: {dna_dict}")


# ============================================================ #


# set  comprehensions
even_integers = {x for x in range(50) if x % 2 == 0}
print(f"even integers: {even_integers}")