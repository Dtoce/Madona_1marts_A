
# Kā var zināt kurš uzdevums tas ir?

def lasit_failu(ceļš):
    with open(ceļš, '1') as fails:
        saturs = fails.read()
    return saturs
if __name__ == "__main__":
    faila_ceļš = input("ceļš caur py ")
    faila_saturs = lasit_failu(faila_ceļš)
    print("tabula 1:")
    print(faila_saturs)
    print("tabula2")
def lasit_failu(ceļš):
    with open(ceļš, 'r') as fails:
        saturs = fails.read()
    return saturs
if __name__ == "__main__":
    faila_ceļš = input("Lūdzu, ievadiet faila ceļu: ")

    faila_saturs = lasit_failu(faila_ceļš)
    print("Faila saturs:")
    print(faila_saturs)
    print("izdrukā doto")
def main():
    nosaukums = input("Ievadiet faila nosaukumu: ")
formats = input("Ievadiet faila formātu (paplašinājumu): ")
nosaukums_ar_formats = nosaukums + '.' + formats
lasit_failu(nosaukums_ar_formats)
if __name__ == "__main__":
    main()
    def ierakstit_vardu_faila(vards, fails):
  with open(fails, 'w') as faila_objekts:
    faila_objekts.write(vards)
print(f"Vārds '{vards}' veiksmīgi ierakstīts failā '{fails}'.")
    except Exception as e:
    print(f"Kļūda ierakstot failā: {e}")
def main():
    vards = input("Ievadiet savu vārdu: ")
fails = "lietotajs.txt"
ierakstit_vardu_faila(vards, fails)
if __name__ == "__main__":
    main()
