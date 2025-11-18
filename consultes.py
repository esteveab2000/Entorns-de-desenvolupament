from ciutats import ciutats

#Demana un codi postal al ususari i l diu de quina ciutat es
codi = int(input("Introdueix un codi postal: "))

for k, v in ciutats.items():
    if v["codi_postal"] == codi:
        print(f"La ciutat amb codi {codi} és {k}.")
        break
else:
    print("Codi postal no trobat.")
