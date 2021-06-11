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

def get_ancestors_recursively(taxon, depth):
    spacer = " " * depth * 4

    def s_print(string):
        print(f"{spacer} {string}")
    
    s_print(f"calculating ancestors for taxon {taxon}")

    if taxon == "Primates":
        s_print("taxon == Primates, returning empty list")
        return []
    else:
        s_print("taxon != Primates, calculating parent")
        parent = tax_dict.get(taxon)
        s_print(f"calculating ancestors for parent {parent}")

        parent_ancestors = get_ancestors_recursively(parent, depth + 1)
        s_print(f"parent ancestors are {str(parent_ancestors)}")

        result = [parent] + parent_ancestors
        s_print(f"returning result {str(result)}")
        return result

print(get_ancestors("Galago alleni"))
print(get_ancestors_recursively("Galago alleni", 0))

