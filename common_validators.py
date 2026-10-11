from datetime import datetime

def validate_date_not_empty(date):
    if date.strip() == "":
        return "date cant be empty"
    return None

def  validate_date_format(date):
    try:
        datetime.strptime(date,"%Y-%m-%d")
        return None
    except ValueError:
        return "wrong format,  format must be (YYYY-mm-dd)"


def validate_subject_not_empty(subject):
    if subject.strip() == "":
        return "subject cant be empty"
    return None


def validate_email_format(email):
    if email.strip() == "":
        return None

    if "@" not in email:
        return "wrong format for  email, format  must be have @ "

    return None