class Plantation:
    def __init__(self,cropy_type,area,planting_date,status,plantation_id = None, harvest_date = None):
        self.plantation_id = plantation_id
        self.cropy_type = cropy_type
        self.area = area
        self.planting_date = planting_date
        self.harvest_date = harvest_date
        self.status = status
