def season(a):
    if a < 0:
        return(print("ti ebanuty?"))
    elif a < 3:
        return(print("zima eto"))
    elif a < 6:
        return(print("vesna branan"))
    elif a < 9:
        return(print("leto, shaslichki"))
    elif a < 12:
        return(print("wto takoe osen - eto etot mesiac"))
    elif a == 12:
        return(print("zima eto"))
    else:
        return (print("ti ebanuty?"))
x = int(input("vvedi nomer mesiaca bratiwka "))
season(x)