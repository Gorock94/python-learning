def bank(a, years):
    i = 0
    while i !=years:
        a = a * 1.1
        i = i + 1
    return(a)
a = int(input('skolko deneg polozhit? '))
years = int(input("na skolko let? "))
print("za ", years, "goda u tebia budet ", bank(a, years), "deneg")