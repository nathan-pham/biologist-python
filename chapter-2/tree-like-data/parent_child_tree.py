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

def get_children(taxon):
    stack = [taxon]
    result = []

    while len(stack) != 0:
        current = stack.pop()
        current_children = tax_dict.get(current, [])
        stack += current_children
        result.append(current)

    return result

def get_children_recursively(taxon):
    result = [taxon]
    children = tax_dict.get(taxon, [])

    for child in children:
        result += get_children_recursively(child)

    return result

print(get_children("Strepsirrhini"))
print(get_children_recursively("Strepsirrhini"))