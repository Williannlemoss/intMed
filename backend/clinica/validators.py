def validate_medico_crm(crm):
    return len(crm) == 10

def validate_medico_nome(nome):
    return nome.isalpha()