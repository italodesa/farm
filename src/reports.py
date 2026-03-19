from files import *

def report_animals():
    animals = view_datas("animals.json")

    print("\nRELATÓRIO DE ANIMAIS")
    print(f"\n|{'ID':7} |{'ESPÉCIE':8} |{'IDADE':10} |{'PESO':7} |{'STATUS':8}")
    print("-" * 80)

    for a in animals:
        id = a["animal_id"]
        species = a["specie"]
        age = f"{a['age']} meses"
        status = f"{a['status']}"
        weight = f"{a['weight']}kg"

        print(f"|{id:<7} |{species:8} |{age:10} |{weight:7} |{status:8}")