from pathlib import Path
import json


def verify(path):
# Função para verificação de arquivos

        # variaveis que vão receber os caminhos dos arquivos
        BASE_DIR = Path(path).resolve().parent.parent
        DATA_DIR = BASE_DIR / "data"
        DATA_FILE = DATA_DIR / path

        #criar a pasta data caso ela não exista
        DATA_DIR.mkdir(exist_ok=True)

        #criar o arquivo caso ele não exista na pasta
        if not DATA_FILE.exists():
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                   json.dump([], f)
        
        #retorna o caminho do arquivo
        return DATA_FILE

def view_datas(a_path):
# Função que retorna o conteudo do arquivo argumentado

    path = verify(a_path)

    with open(path,"r",encoding="utf-8") as f:
            all_data = json.load(f)

    return all_data

def generate_id(a_path,id_object):
# Função que gera Ids únicos para os objetos

        path = verify(a_path)
        all_data = view_datas(path)

        if all_data:
        # Pega o maior ID e soma 1
            next_id = max(a[id_object] for a in all_data) + 1
        else:
            next_id = 1  # Primeiro ID

        return next_id

def write_file(a_path, data):
# Função para escrever dados no arquivo

    path = verify(a_path)
    all_data = view_datas(a_path)
    all_data.append(data)

    with open(path,"w",encoding="utf-8") as f:
            json.dump(all_data, f, indent=4, ensure_ascii=False)