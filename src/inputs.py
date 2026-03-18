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

    @staticmethod
    def print_all_inputs():
        print_formatted_data("inputs.json")

    @staticmethod
    def inputs_menu():
        while True:
            print("=" * 50)
            print(" " * 15 + "Sistema de Insumos" + " " * 15 )
            print("=" * 50)

            print("[1] Criar insumo\n[2] Listar insumos\n[3] Atualizar insumo\n"
            "[4] Remover insumo\n[5] Adicionar estoque\n[6] Retirar estoque\n"
            "[7] Buscar insumos\n[0] Voltar")

            asw = int(input(">>> "))

            match asw:
                case 0:
                    break
            
                case 1:
                    Input.create_input_object()

                case 2:
                    Input.print_all_inputs()

                case 3:
                    pass

                case 4:
                    pass

                case 5:
                    pass

                case 6:
                    pass

                case 7:
                    pass
                case _:
                    print("Digite uma opção valida")