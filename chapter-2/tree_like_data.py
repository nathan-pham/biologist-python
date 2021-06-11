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

taxonomy = { 
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
        ancestor = taxonomy.get(taxon)
        result.append(ancestor)
        taxon = ancestor

    return result

print(get_ancestors("Galago alleni"))