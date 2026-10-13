from datetime import datetime

def count_customers(connection):
    sql = "SELECT COUNT(*) FROM customers WHERE is_deleted = 0 "
    cursor = connection.cursor()
    cursor.execute(sql,)
    result = cursor.fetchone()
    return result[0]



def count_open_follow_ups(connection):
    sql = "SELECT COUNT(*) FROM follow_ups WHERE status = ?"
    cursor = connection.cursor()
    cursor.execute(sql,("undone",))
    result = cursor.fetchone()
    return result[0]
    
def count_today_follow_ups(connection):
    today = datetime.now().strftime("%Y-%m-%d")
    sql = "SELECT COUNT(*) FROM follow_ups WHERE status = ? AND date = ?"
    cursor = connection.cursor()
    cursor.execute(sql,("undone",today))
    result = cursor.fetchone()
    return result[0]
def count_interactions(connection):
    sql = "SELECT COUNT(*) FROM interactions"
    cursor = connection.cursor()
    cursor.execute(sql,)
    result = cursor.fetchone()
    return result[0]