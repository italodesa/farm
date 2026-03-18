from files import *

class Input:
    def __init__(self,name,quantity,unit,category,input_id = None):
        self.input_id = input_id
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.category = category

    @classmethod
    def create_input_object(cls):
        while True:
            try:
                name = input("Digite o nome do insumo: ")
                quantity = float(input("Digite a quantidade do insumo: "))
                unit = input("Digite a unidade de medida do insumo: ")
                category = input("Digite a categoria do insumo "
                "(ex: feed, fertilizer, seed, etc.): ")
                input_id = generate_id("inputs.json", "input_id")
                break
            except ValueError:
                print("Entrada inválida. Por favor, tente novamente.")
        input_object = cls(name, quantity, unit, category, input_id)
        write_file("inputs.json", input_object.__dict__)

Input.create_input_object()