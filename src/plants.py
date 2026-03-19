from files import *
from datetime import datetime, timedelta
from movements import register_movement

class Plantation:
    def __init__(self,crop_type,area,planting_date,status,plantation_id = None, harvest_date = None):
        self.plantation_id = plantation_id
        self.crop_type = crop_type

        self.area = area
        self.planting_date = planting_date
        self.harvest_date = harvest_date
        self.status = status

    def calculate_harvest(self):
    # convert ISO string to date
        planting_date = datetime.fromisoformat(self.planting_date)

        days = crops.get(self.crop_type)
        if days is None:
            return None
        
        harvest_date = planting_date + timedelta(days=days)

        return str(harvest_date.date())
    
    def edit_plantation(self,attribute,value):
        delete_data("plants.json", self.plantation_id, "plantation_id")
        setattr(self, attribute, value)
        write_file("plants.json", self.__dict__)

    def view_plantation(self):
        print(f"ID: {self.plantation_id}")
        print(f"Tipo de cultura: {self.crop_type}")
        print(f"Área: {self.area} hectares")
        print(f"Data de plantio: {self.planting_date}")
        print(f"Data de colheita: {self.harvest_date}")
        print(f"Status: {self.status}")
        print("\n")

    @classmethod
    def create_plantation(cls):
        while True:
            try:
                crop_type = input("informe o tipo de cultura plantada (ex: “milho”, “soja”): ").strip().lower()
                area = float(input("informe o tamanho da área cultivada em hectares: "))
                planting_date = input("Digite a data de plantio (YYYY-MM-DD): ")
                datetime.fromisoformat(planting_date)  # validação
                status = input("Situação atual da cultura (planted, harvested, rotated, inactive): ")
                plantation_id = generate_id("plants.json","plantation_id")
                break
            except ValueError:
                print("Entrada inválida. Por favor, tente novamente.")
        
        plantation = cls(crop_type, area, planting_date, status, plantation_id)
        plantation.harvest_date = plantation.calculate_harvest()

        if plantation.harvest_date is None:
            print("Tipo de cultura desconhecido. Não foi possível calcular a data de colheita.")
            return None
        
        write_file("plants.json", plantation.__dict__)

    @classmethod
    def recover_plantation(cls):
        id = int(input("Digite o ID da plantação: "))
        plantation_data = recover_obj_data("plants.json", id, "plantation_id")

        if plantation_data:
            return cls(
                plantation_data["crop_type"],
                plantation_data["area"],
                plantation_data["planting_date"],
                plantation_data["status"],
                plantation_data["plantation_id"]
            )
        else:
            print("ID não encontrado.")
            return None

    @staticmethod
    def print_all_plantations():
        print_formatted_data("plants.json")

    @staticmethod
    def plants_menu():
        while True:
            print("=" * 50)
            print(" " * 15 + "Sistema de plantações" + " " * 15 )
            print("=" * 50)

            print("[1] Criar plantação\n[2] Listar plantações\n[3] Atualizar status\n"
            "[4] Remover plantação\n[5] Relatorios de plantação\n[6] Registro de movimentação\n"
            "[7] Buscar plantações\n[0] Voltar")

            asw = int(input(">>> "))

            match asw:
                case 0:
                    break
            
                case 1:
                    Plantation.create_plantation()

                case 2:
                    Plantation.print_all_plantations()

                case 3:
                    Plantation.edit_plantation_menu()

                case 4:
                    id = int(input("Digite o ID da plantação a ser deletada: "))
                    delete_data("plants.json", id, "plantation_id")

                case 5:
                    pass

                case 6:
                    pass

                case 7:
                    all_plantations = view_datas("plants.json")
                    crop_type = input("Digite o tipo de cultura para buscar: ").strip().lower()
                    id_plantation = int(input("Digite o ID da plantação para buscar: "))

                    for plantation in all_plantations:
                        if plantation["crop_type"] == crop_type or plantation["plantation_id"] == id_plantation:
                            print(f"{'Campo':<15} | {'Valor':<15}")
                            print("-" * 32)
                            for chave, valor in plantation.items():
                                print(f"{chave:<15} | {valor:<15}")
                            print("\n")

                case _:
                    print("Digite uma opção valida")

    @staticmethod
    def edit_plantation_menu():
        while True:
            try:
                print("=" * 50)
                print(" " * 15 + "Editar plantação" + " " * 15 )
                print("=" * 50)
                print("[1] Editar tipo de cultura\n[2] Editar área\n[3] Editar " \
                "data de plantio\n[4] Editar status\n[0] Voltar")
                asw = int(input(">>> "))

                match asw:
                    case 0:
                        break
                    
                    case 1:
                        plantation = Plantation.recover_plantation()
                        new_crop_type = input("Digite o novo tipo de cultura: ")
                        plantation.edit_plantation("crop_type", new_crop_type)
                        
                    case 2:
                        plantation = Plantation.recover_plantation()
                        new_area = float(input("Digite a nova área: "))
                        plantation.edit_plantation("area", new_area)

                    case 3:
                        plantation = Plantation.recover_plantation()
                        new_planting_date = input("Digite a nova data de plantio: ")
                        plantation.edit_plantation("planting_date", new_planting_date)

                    case 4:
                        plantation = Plantation.recover_plantation()
                        new_status = input("Digite o novo status (planted, harvested, rotated, inactive): ")
                        plantation.edit_plantation("status", new_status)
                        if plantation.status == "harvested":
                            register_movement(
                                "plantation",
                                plantation.plantation_id,
                                f"Plantação colhida: {plantation.crop_type}"
                            )

                    case _:
                        print("Digite uma opção valida")
            except Exception:
                print(f"Erro. A plantação não existe. Por favor, tente novamente.")

crops = {
    "milho": 120,
    "alface": 45,
    "soja": 110,
    "arroz": 130,
    "feijao": 90,
    "trigo": 120,
    "cebola": 150,
    "batata": 100,
    "cenoura": 80,
    "repolho": 90,
    "tomate": 90,
    "pepino": 60,
    "abobora": 100,
    "melancia": 85,
    "melao": 75,
    "couve": 70,
    "brocolis": 85,
    "pimentao": 100,
    "berinjela": 110,
    "cana_de_acucar": 365
}