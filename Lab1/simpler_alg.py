from Lab1.main_alg import *
def spr_vyraz(A,B,C,U):
    return set(notX(A, U) | notX(C, U) | notX(B, U))
