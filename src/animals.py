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