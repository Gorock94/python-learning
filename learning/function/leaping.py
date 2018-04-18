def leaps(a):
    if (a % 400 == 0 or (a % 100 != 0 and a % 4 == 0)):
        return(1)
    else:
        return(0)