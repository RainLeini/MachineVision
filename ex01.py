def juhised():
    print("Koordinaadid.")
    print("Sisestage ridade ja tulpade arv (positiivsed täisarvud).")


def sisendi_kontroll(sisend):
    """Kontrollib, kas sisend on positiivne täisarv."""
    try:
        arv = int(sisend)
        if arv > 0:
            return arv
        else:
            print("Palun sisestage positiivne täisarv.")
            return None
    except ValueError:
        print("Sisend ei sobi. Palun sisestage täisarv.")
        return None


def genereeri_muster(ridade_arv, tulpade_arv):
    for rida in range(ridade_arv):
        if rida % 2 == 0:
            print("#" + "X#" * tulpade_arv)
        else:
            print("##" + "X##" * (tulpade_arv - 1) + "X##")


def pea():
    juhised()
    while True:
        ridade_sisend = input("Sisestage ridade arv: ")
        ridade_arv = sisendi_kontroll(ridade_sisend)

        tulpade_sisend = input("Sisestage tulpade arv: ")
        tulpade_arv = sisendi_kontroll(tulpade_sisend)

        if ridade_arv and tulpade_arv:
            print("\nGenereeritud muster:")
            genereeri_muster(ridade_arv, tulpade_arv)
            break

pea()
