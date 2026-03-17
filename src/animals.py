from files import generate_id,write_file

class Animal:
    def __init__(self,specie, age, weight, status,animal_id = None):
        self.animal_id = animal_id
        self.specie = specie
        self.age = age
        self.weight = weight
        self.status = status

    @classmethod
    def create_animal(cls):
        while True:
            try:
                specie = input("Digite a especie do animal: ")
                age = int(input("Digite a idade do animal: "))
                weight = float(input("Digite o peso do animal: "))
                status = input("Digite o status do animal: ")
                animal_id = generate_id("animals.json","animal_id")
                break
            except ValueError:
                print("Entrada inválida. Por favor, tente novamente.")
        
        animal = cls(specie, age, weight, status, animal_id)
        write_file("animals.json", animal.__dict__)

    @staticmethod
    def animals_menu():
        while True:
            
            print("=" * 50)
            print(" " * 15 + "Animais" + " " * 15 )
            print("=" * 50)
            print("[1] Cadastrar animal\n[2] Editar animal\n[3] Relatorio \n[4] " \
            "Pesquisar\n[0] Voltar")
            asw = int(input(">>> "))

            match asw:
                case 0:
                    break
                
                case 1:
                    Animal.create_animal()
                    
                case 2:
                    pass

                case 3:
                    pass

                case 4:
                    pass
                
                case _:
                    print("Digite uma opção valida")