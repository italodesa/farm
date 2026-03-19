from animals import Animal
from plants import Plantation  
from inputs import Input

while True:
    print("=" * 50)
    print(" " * 15 + "fazenda digital" + " " * 15 )
    print("=" * 50)
    print("[1] Animais\n[2] Plantações\n[3] Insumos \n[4] Relatório geral\n[0] Encerrar")
    try:
        asw = int(input(">>> "))

        match asw:
            case 0:
                break

            case 1:
                Animal.animals_menu()

            case 2:
                Plantation.plants_menu()

            case 3:
                Input.inputs_menu()

            case 4:
                pass

            case _:
                print("Digite uma opção valida")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")