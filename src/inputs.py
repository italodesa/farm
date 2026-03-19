from files import *

class Input:
    def __init__(self,name,quantity,unit,category,input_id = None):
        self.input_id = input_id
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.category = category

    def add_quantity(self, amount):
        if amount < 0:
            print("A quantidade a ser adicionada deve ser positiva.")
            return
        delete_data("inputs.json", self.input_id, "input_id")
        self.quantity += amount
        write_file("inputs.json", self.__dict__)

    def remove_quantity(self, amount):
        if amount < 0:
            print("A quantidade a ser removida deve ser positiva.")
            return
        if amount > self.quantity:
            print("Quantidade insuficiente no estoque.")
            return
        delete_data("inputs.json", self.input_id, "input_id")
        self.quantity -= amount
        write_file("inputs.json", self.__dict__)

    def edit_input(self, attribute, value):
        delete_data("inputs.json", self.input_id, "input_id")
        setattr(self, attribute, value)
        write_file("inputs.json", self.__dict__)

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

    @classmethod
    def recover_input(cls):
        id = int(input("Digite o ID do insumo: "))
        input_data = recover_obj_data("inputs.json", id, "input_id")

        if input_data:
            return cls(
                input_data["name"],
                input_data["quantity"],
                input_data["unit"],
                input_data["category"],
                input_data["input_id"]
            )
        else:
            print("ID não encontrado.")
            return None

    @staticmethod
    def print_all_inputs():
        print_formatted_data("inputs.json")

    @staticmethod
    def search_inputs():
        all_inputs = view_datas("inputs.json")
        input_name = input("Digite o nome do insumo para buscar: ")
        try:
            input_id = int(input("Digite o ID do insumo para buscar: "))

            for input_item in all_inputs:
                if input_item.get("name") == input_name or input_item.get("input_id") == input_id:
                    print(f"{'Campo':<15} | {'Valor':<15}")
                    print("-" * 32)
                    for chave, valor in input_item.items():
                        print(f"{chave:<15} | {valor:<15}")
                    print("\n")

        except ValueError:
            print("Entrada inválida. Por favor, tente novamente.")
        except UnboundLocalError:
            print("Nenhum insumo encontrado com os critérios fornecidos.")

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
                    Input.edit_input_menu()

                case 4:
                    id = int(input("Digite o ID do insumo a ser removido: "))
                    delete_data("inputs.json", id,"input_id")

                case 5:
                    input_obj = Input.recover_input()
                    if input_obj:
                        quantity = float(input("Digite a quantidade a ser adicionada: "))
                        input_obj.add_quantity(quantity)

                case 6:
                    input_obj = Input.recover_input()
                    if input_obj:
                        quantity = float(input("Digite a quantidade a ser retirada: "))
                        input_obj.remove_quantity(quantity)

                case 7:
                    Input.search_inputs()
                case _:
                    print("Digite uma opção valida")
    
    @staticmethod
    def edit_input_menu():
        while True:
            print("=" * 50)
            print(" " * 15 + "Editar Insumo" + " " * 15 )
            print("=" * 50)
            print("[1] Editar nome\n[2] Editar categoria\n[3] " \
            "editar unidade de medida\n[0] Voltar")
            asw = int(input(">>> "))
            match asw:
                case 0:
                    break
                case 1:
                    input_obj = Input.recover_input()
                    if input_obj:
                        new_name = input("digite o novo nome do insumo:")
                        input_obj.edit_input("name", new_name)
                case 2:
                    input_obj = Input.recover_input()
                    if input_obj:
                        new_category = input("digite a nova categoria do insumo: ")
                        input_obj.edit_input("category", new_category)
                case 3:
                    input_obj = Input.recover_input()
                    if input_obj:
                        new_unit = input("digite a nova unidade de medida do insumo: ")
                        input_obj.edit_input("unit", new_unit)
                case _:
                    print("Digite uma opção valida")
