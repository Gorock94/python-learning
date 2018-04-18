def is_prime(x):
    i = 2
    while i != x:
        if x % i == 0:
            return(print("popalsia! slowno!"))
            break
        else:
            return(print("chislo pro100e"))
a = int(input("vvedi chislo "))
is_prime(a)