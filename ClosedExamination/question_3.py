ATOMS = {
    'H': {'name': 'Hydrogen', 'weight': 1.00797},
    'He': {'name': 'Helium', 'weight': 4.00260},
    'C': {'name': 'Carbon', 'weight': 12.011},
    'N': {'name': 'Nitrogen', 'weight': 14.0067},
    'O': {'name': 'Oxygen', 'weight': 15.9994},
    'Ca': {'name': 'Calium', 'weight': 40.08}
    }


def molar_mass(molecule: list) -> float:
    """Gets the molar mass of a molecule

    Args:
        molecule (list): A molecule defined by a list of tuples

    Raises:
        ValueError: If the molecule contains an unknown element

    Returns:
        float: The molar mass of the molecule
    """
    total_mass = 0.0
    for element in molecule:
        if element[0] not in ATOMS.keys():
            raise ValueError
        weight = ATOMS.get(element[0]).get("weight")
        total_mass += weight * element[1]
    return total_mass
