import re

def cpfValidate(document_number):
    cpf = str(document_number)
    cpf = re.sub(r'[^0-9]', '', cpf)

    if not cpf or len(cpf) != 11:
        return False

    # eliminate two final cpf number
    new_cpf = cpf[:-2]

    reverse_count = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9

        total += int(new_cpf[index]) * reverse_count

        reverse_count -= 1
        if reverse_count < 2:
            reverse_count = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            new_cpf += str(d)

    sequence = new_cpf == str(new_cpf[0]) * len(cpf)

    if cpf == new_cpf and not sequence:
        return True
    else:
        return False