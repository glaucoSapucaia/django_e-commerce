import re

def cepValidate(cep):
    if re.search(r'[^0-9]', cep) or len(cep) < 8:
        return False
    return True