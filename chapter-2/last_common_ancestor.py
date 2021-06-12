tax_dict = {
    "Primates": ["Haplorrhini", "Strepsirrhini"], 
    "Tarsiiformes": ["Tarsius tarsier"], 
    "Haplorrhini": ["Tarsiiformes", "Simiiformes"], 
    "Simiiformes": ["Hominoidea"], 
    "Lorisidae": ["Loris tardigradus"], 
    "Lemuriformes": ["Allocebus trichotis"], 
    "Lorisiformes": ["Galago alleni","Galago moholi"], 
    "Hominoidea": ["Pongo abelii", "Pan troglodytes"], 
    "Strepsirrhini": ["Lorisidae", "Lemuriformes", "Lorisiformes"] 
}

def get_ancestors_recursively(taxon):
    if taxon == "Primates":
        return []
    else:
        parent = tax_dict.get(taxon)
        parent_ancestors = get_ancestors_recursively(parent)
        result = [parent] + parent_ancestors
        return result

def get_lca(taxon_a, taxon_b):
    ancestors_a = [taxon_a] + get_ancestors_recursively(taxon_a)
    ancestors_b = [taxon_b] + get_ancestors_recursively(taxon_b)

    for taxon in ancestors_b:
        if taxon in ancestors_a:
            return taxon

