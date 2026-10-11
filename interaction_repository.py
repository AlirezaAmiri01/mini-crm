import sqlite3
from interaction_validators import validate_type_not_empty,validate_type_in_list
from common_validators import validate_date_not_empty,validate_date_format,validate_subject_not_empty
class InteractionRepository:
    def __init__(self,connection):
        self.connection = connection



    def get_by_customer_id(self,customer_id):
        sql = "SELECT * FROM interactions WHERE customer_id = ?"
        cursor = self.connection.cursor()
        cursor.execute(sql,(customer_id,))
        return cursor.fetchall()


    def add_interaction(self,customer_id,type,date,subject,notes,result):
        error = validate_date_not_empty(date)
        if error:
            return error

        error = validate_date_format(date)
        if error:
            return error


        error = validate_type_not_empty(type)
        if error:
            return error

        error = validate_type_in_list(type)
        if error:
            return error

        error = validate_subject_not_empty(subject)
        if error:
            return error
                
        try:
            sql="""  
            INSERT INTO interactions(
            customer_id,
            type,
            date,
            subject,
            notes,
            result  
            )
            VALUES(
            ?,?,?,?,?,?) 
            """

            cursor = self.connection.cursor()
            cursor.execute(sql,(customer_id,type,date,subject,notes,result))
            self.connection.commit()

        except sqlite3.Error as e:
            print("database error: ",e)
            return f"database error: {e}"


    def update_interaction(self,interaction_id,type,date,subject,notes,result):
        error = validate_date_not_empty(date)
        if error: 
            return error 

        error = validate_date_format(date)
        if error:
            return error

        error = validate_type_not_empty(type)
        if error:
            return error

        error = validate_type_in_list(type)
        if error:
            return error

        error = validate_subject_not_empty(subject)
        if error:
            return error 
          
        try:        
            sql = "UPDATE interactions SET type=?,date=?,subject=?,notes=?,result=? WHERE id=?"
            cursor = self.connection.cursor( )
            cursor.execute(sql,(type,date,subject,notes,result,interaction_id))
            self.connection.commit()

        except sqlite3.Error as e:
            print("database error: ",e)
            return f"database error: {e}"



    def delete(self,interaction_id):


    
           
        try:   
            sql = "DELETE FROM interactions WHERE id=?"
            cursor = self.connection.cursor()
            cursor.execute(sql,(interaction_id,))
            self.connection.commit()

        except sqlite3.Error as e:
            print("database error: ",e)
            return f"database error: {e}"


