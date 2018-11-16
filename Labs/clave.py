def valida_numero_caracteres(password):
    if len(password) <= 7:
        return False
    else:
        return True

def valida_alfa(password):
    if password.isalnum():
        return True
    return False
        
def validar_space(password):
    for s in password:
        if s.isspace() == True:
            return False
    return True
                

def valida_upper(password):
    """ Valida las reglas solicitadas, retorna 1 en ok o 2 fail"""
    for s in password:
        if s.isupper() == True:
                return True
    return False

def valida_lower(password):
    """ Valida las reglas solicitadas, retorna 1 en ok o 2 fail"""
    for s in password:
        if s.islower() == True:
                return True
    return False


def valida_digito(password):
    """ Valida las reglas solicitadas, retorna 1 en ok o 2 fail"""
    for s in password:
        if s.isdigit() == True: 
            return True
    return False

def valida_clave(password):
    set1 = { valida_numero_caracteres(password), valida_alfa(password),
            valida_digito(password),
            valida_lower(password),
            valida_upper(password)  }
    if len(set1) == 1:
        print ("contrasena Valida: ")
    else:
        print ("contrasena no valida")
        

def main():
    password = input("Ingrese password: ")
    print(valida_clave(password))
    
if __name__ == '__main__':
    main()
