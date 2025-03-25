#tento kód nahoře tady nech a neopakuj ho

#podokončení programu se zeptejte, zda chce uživatel celý program opakovat
#pokud ano spusťte znovu pokud ne ukončete programsi
import random
 
zvirata = [
    "kočka", "pes", "slon", "žirafa", "lev", "tygr", "sova",
    "tučňák", "ježek", "králík", "myš", "medvěd", "vlk", "liška",
    "klokan", "chameleon", "opice", "panda", "lenochod", "velbloud"
]
 
while True:
    nahodne_zvire = random.choice(zvirata)
    print(f'Náhodné zvíře: {nahodne_zvire}')
    
    opakovat = input("Chcete pokračovat? (ano/ne): ").strip().lower()
    if opakovat != "ano":
        break


