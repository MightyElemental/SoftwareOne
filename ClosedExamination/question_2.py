import re


def molecule_to_list(molecule: str) -> list:
    """Splits up a molucule into elements and amount in order of appearance

    Args:
        molecule (str): The molecule to split up

    Raises:
        ValueError: If molecule starts with a lower case letter
        ValueError: If molecule contains a non-alphanumeric character
        ValueError: If an element starts with a lower case letter

    Returns:
        list: A list of tuples containing the element symbol and the number of
        its appearances at that position
    """
    if molecule[0].islower():
        raise ValueError
    # Test if molecule contains non-alphanumeric characters
    if re.match(r"^[\w]+$", molecule) is None:
        raise ValueError
    result = []
    # Split molecule into elements and amounts
    elements = re.findall(r"([A-Z][a-z]?|[a-z]{1,2})(\d{1,2})?", molecule)
    for element in elements:
        if element[0].islower():
            raise ValueError
        # Ensure the result has a numerical value
        if element[1] == '':
            result.append((element[0], 1))
        else:
            result.append((element[0], int(element[1])))
    return result
