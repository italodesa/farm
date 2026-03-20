from datetime import datetime
from files import write_file

def register_movement(entity_type, obj_id, action):

    event = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": entity_type,
        "id": obj_id,
        "action": action,
    }

    write_file("movements.json", event)