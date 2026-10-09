def validate_phone_not_dupliacte(phone,connection,customer_id):
    cursor = connection.cursor()
    sql = "SELECT * FROM customers WHERE phone=? AND id != ?"
    cursor.execute(sql,(phone,customer_id))
    result = cursor.fetchone()

    if result:
        return "this phone already exsist"
    else:
        return None
    