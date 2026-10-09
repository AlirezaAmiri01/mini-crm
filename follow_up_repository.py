import sqlite3
class FollowUpRepository:
    def __init__(self,connection):
        self.connection = connection


    def get_by_customer_id(self,customer_id):
        sql = "SELECT * FROM follow_ups WHERE customer_id=?"
        cursor = self.connection.cursor()
        cursor.execute(sql,(customer_id,))
        return cursor.fetchall()


    def add_follow_up(self,customer_id,date,subject,description):
        try:
            sql = """
            INSERT INTO follow_ups(
            customer_id,
            date,
            subject,
            description, 
            status
            )
            VALUES(?,?,?,?,?)
            """
            cursor = self.connection.cursor() 
            cursor.execute(sql,(customer_id,date,subject,description,"undone"))
            self.connection.commit()

        except sqlite3.Error as e:
            print("database error: ",e)
            return f"database error: {e}"



    def update_follow_up(self,follow_up_id,date,subject,description,status):
        try:
            sql = "UPDATE follow_ups SET date=?,subject=?,description=?,status=? WHERE id=?"
            cursor = self.connection.cursor()
            cursor.execute(sql,(date,subject,description,status,follow_up_id))
            self.connection.commit()

        except sqlite3.Error as e:
            print("database error: ",e)
            return f"database error: {e}"


    def delete_follow_up(self,follow_up_id):
        try:
            sql = "DELETE From follow_ups WHERE id=?"
            cursor = self.connection.cursor()
            cursor.execute(sql,(follow_up_id,))
            self.connection.commit()

        except sqlite3.Error as e:
            print("database error: ", e)
            return f"database error: {e}"

    def switch_status(self,follow_up_id,current_status):
        try:    
            if current_status == "done":
                current_status = "undone"
            else:
                current_status = "done"

            sql = "UPDATE follow_ups SET status=? WHERE id=?"
            cursor = self.connection.cursor()
            cursor.execute(sql,(current_status,follow_up_id))
            self.connection.commit()


        except sqlite3.Error as e:
            print("database error: ", e)
            return f"database error: {e}"
