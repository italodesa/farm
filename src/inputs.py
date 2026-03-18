class Input:
    def __init__(self,name,quantity,unit,category,input_id = None):
        self.input_id = input_id
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.category = category