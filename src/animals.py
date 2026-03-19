from files import *
from movements import register_movement

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

    def edit_animal(self,attribute,value):
        delete_data("animals.json", self.animal_id, "animal_id")
        setattr(self, attribute, value)
        write_file("animals.json", self.__dict__)

    @classmethod
    def create_animal(cls):
        while True:
            try:
                specie = input("Digite a especie do animal: ")
                age = int(input("Digite a idade do animal: "))
                weight = float(input("Digite o peso do animal (em kg): "))
                status = input("Digite o status do animal (active, sold ou death): ")
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
                    Animal.edit_animal_menu()

                case 3:
                    Animal.print_all_animals()

                case 4:
                    animal = Animal.recover_animal()
                    if animal:
                        animal.view_animal()
                
                case _:
                    print("Digite uma opção valida")

    @staticmethod
    def edit_animal_menu():
        while True:
            try:
                print("=" * 50)
                print(" " * 15 + "Editar animal" + " " * 15 )
                print("=" * 50)
                print("[1] Editar especie\n[2] Editar" \
                " idade\n[3] Editar peso\n[4] Editar status\n[0] Voltar")
                asw = int(input(">>> "))

                match asw:
                    case 0:
                        break
                    
                    case 1:
                        animal = Animal.recover_animal()
                        new_specie = input("Digite a nova especie: ")
                        animal.edit_animal("specie", new_specie)
                        
                    case 2:
                        animal = Animal.recover_animal()
                        new_age = int(input("Digite a nova idade: "))
                        animal.edit_animal("age", new_age)

                    case 3:
                        animal = Animal.recover_animal()
                        new_weight = float(input("Digite o novo peso (em kg): "))
                        animal.edit_animal("weight", new_weight)

                    case 4:
                        animal = Animal.recover_animal()
                        new_status = input("Digite o novo status (active, sold ou death): ")
                        animal.edit_animal("status", new_status)
                        if animal.status == "sold":
                            register_movement("animal", animal.animal_id, f"sold animal:" \
                            f" {animal.specie}")

                    case _:
                        print("Digite uma opção valida")
            except Exception:
                print(f"Erro. O animal não existe. Por favor, tente novamente.")