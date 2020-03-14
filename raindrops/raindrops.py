def convert(numero):
    pal = ""
    num = {3:"Pling", 5:"Plang", 7:"Plong"}
    for key, value in num.items():
        if numero%key==0:
            pal+=value
    if pal == "":
        pal+=(str(numero))
    return pal