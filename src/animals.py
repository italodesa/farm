from files import *

class Animal:
    def __init__(self,specie, age, weight, status,animal_id = None):
        self.animal_id = animal_id
        self.specie = specie
        self.age = age
        self.weight = weight
        self.status = status

    def view_animal(self):
        print(f"ID: {self.animal_id}")
        print(f"Especie: {self.specie}")
        print(f"Idade: {self.age}")
        print(f"Peso: {self.weight}")
        print(f"Status: {self.status}")

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

    @classmethod
    def recover_animal(cls):
        id = int(input("Digite o ID do animal: "))
        animal_data = recover_obj_data("animals.json", id, "animal_id")

        if animal_data:
            return cls(
                animal_data["specie"],
                animal_data["age"],
                animal_data["weight"],
                animal_data["status"],
                animal_data["animal_id"]
            )
        else:
            print("ID não encontrado.")
            return None

    @staticmethod
    def print_all_animals():
        print_formatted_data("animals.json")
        

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
                    Animal.print_all_animals()

                case 4:
                    pass
                
                case _:
                    print("Digite uma opção valida")