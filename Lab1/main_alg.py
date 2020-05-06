def notX(X,U):
    nX = set(U)
    for elem in X:
        if elem in nX:
            nX.remove(elem)
    return nX


def vyraz(A,B,C,U):
    return set(notX(A,U) | notX(B,U) | (notX(A,U) & B) | (notX(B,U) & C) | notX(C,U))
