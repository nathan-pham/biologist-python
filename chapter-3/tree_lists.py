tree = ['dog', 
    ['raccoon','bear'], 
    [
        ['sea_lion','seal'],
        ['monkey','cat'], 
        'weasel'
    ]
]

def includes(tree, element):
    for leaf in tree:
        if leaf == element or (includes(leaf, element) if isinstance(leaf, list) else False):
            return True

    return False

print(includes(tree, "seals"))