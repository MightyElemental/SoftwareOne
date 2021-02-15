def check_level(level: list):
    # If on last element, and its not zero, level is feasable
    if len(level) == 1:
        return level[0] != 0
    # call check_level for each jump amount at the current position
    # with a maximum jump up to the last element
    for i in range(min(level[0], len(level)-1)):
        flag = check_level(level[i+1:])
        if flag:
            return True
    return False
