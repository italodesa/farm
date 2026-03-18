from files import *
from datetime import datetime, timedelta

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