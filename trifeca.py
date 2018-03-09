def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    double = 0
    ind = 0
    while ind < (len(word)-1):
        if word[ind] == word[ind+1]:
            double = double+1
            ind = ind+2
        else:
            ind = ind+1
            double = 0 
    if double >= 3:
        return True
    return False


