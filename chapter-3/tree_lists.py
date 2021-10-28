tree = [
    'dog', 
    ['raccoon','bear'], 
    [
        ['sea_lion','seal'],
        ['monkey','cat'], 
        'weasel'
    ]
]

# check if element is present in a tree-like list
def includes(tree, element):
    for leaf in tree:
        if leaf == element or (includes(leaf, element) if isinstance(leaf, list) else False):
            return True

    return False

print(includes(tree, "seal"))

# retrieve sublists that contain a taxon
def sublist(tree, taxon):
    results = []

    if includes(tree, taxon):
        results.append(tree)

    for leaf in tree:
        if isinstance(leaf, list):
            results.extend(sublist(leaf, taxon))

    return results

print("\n".join([f"{ leaf } includes monkey" for leaf in sublist(tree, "monkey")]))