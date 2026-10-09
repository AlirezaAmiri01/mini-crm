def validate_name_not_empty(name):
    if name.strip() == "":
        return "Name cannot be empty"
    return None

def validate_name_not_number(name):
    if name.strip().isdigit():
        return "Name cannot be only numbers"
    return None



def validate_phone_not_empty(phone):
    if phone.strip() =="":
        return "phone cannot empty"
    return None

def validate_phone(phone):
    if len(phone.strip()) != 11 or  not  phone.strip().startswith("09"):
        return "invalid phone number"
    return None    


def validate_phone_not_word(phone):
    if not phone.isdigit():
        return "phone must be a number "
    return None

