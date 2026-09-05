class InteractionRepository:
    def __init__(self,connection):
        self.connection = connection



    def get_by_customer_id(self,customer_id):
        sql = "SELECT * FROM interactions WHERE customer_id = ?"
        cursor = self.connection.cursor()
        cursor.execute(sql,(customer_id,))
        return cursor.fetchall()


    def add_interaction(self,customer_id,type,date,subject,notes,result):
        sql="""  
        INSERT INTO interactions(
        customer_id,
        type,
        date,
        subject,
        notes,
        result  
        )
        VALUES(?,?,?,?,?,?) 
        """

        cursor = self.connection.cursor()
        cursor.execute(sql,(customer_id,type,date,subject,notes,result))
        self.connection.commit()


    def update_interaction(self,interaction_id,type,date,subject,notes,result):
        sql = "UPDATE interactions SET type=?,date=?,subject=?,notes=?,result=? WHERE id=?"
        cursor = self.connection.cursor( )
        cursor.execute(sql,(type,date,subject,notes,result,interaction_id))
        self.connection.commit()


    def delete(self,interaction_id):
        sql = "DELETE FROM interactions WHERE id=?"
        cursor = self.connection.cursor()
        cursor.execute(sql,(interaction_id,))
        self.connection.commit()