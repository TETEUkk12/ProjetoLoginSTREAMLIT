import json
import os

USUARIOS = "data/usuarios.json"

def load_usuarios():
    if os.path.exists(USUARIOS):
        with open(USUARIOS, "r", encoding="utf-8") as ark_json:
            return json.load(ark_json)
    else:
        return []