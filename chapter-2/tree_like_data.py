"""
Primate Taxa

Primates
    Haplorrhini
        Simiiformes
            Hominoidea
                Pan troglodytes
                Pongo abelii
        Tarsiiformes
            Tarsius tarsier
    Strepsirrhini
        Lorisidae
            Loris tardigradus
        Lemuriformes
            Allocebus trichotis
        Lorisiformes
            Galago alleni
            Galago moholi
"""

tax_dict = { 
    "Pan troglodytes": "Hominoidea", "Pongo abelii": "Hominoidea", 
    "Hominoidea": "Simiiformes", "Simiiformes": "Haplorrhini", 
    "Tarsius tarsier": "Tarsiiformes", "Haplorrhini": "Primates",
    "Tarsiiformes": "Haplorrhini", "Loris tardigradus": "Lorisidae",
    "Lorisidae": "Strepsirrhini", "Strepsirrhini": "Primates",
    "Allocebus trichotis": "Lemuriformes", "Lemuriformes": "Strepsirrhini",
    "Galago alleni": "Lorisiformes", "Lorisiformes": "Strepsirrhini",
    "Galago moholi": " Lorisiformes"
} 

def get_ancestors(taxon):
    result = []

    while taxon != "Primates":
        parent = tax_dict.get(taxon)

        result.append(parent)
        taxon = parent

    return result

def get_ancestors_recursively(taxon):
    if taxon == "Primates":
        return []
    else:
        parent = tax_dict.get(taxon)
        parent_ancestors = get_ancestors_recursively(parent)
        return [parent] + parent_ancestors

print(get_ancestors("Galago alleni"))
print(get_ancestors_recursively("Galago alleni"))

