
def validate_type_not_empty(type):
    if type.strip() == "":
        return "type cant be empty"
    return None

def validate_type_in_list(type):
    types_list = ["call","meeting","email","message","other"]

    if type not in types_list:
        return "wrong type, type must be in list (call,meeting,email,message,other)"
    return None

