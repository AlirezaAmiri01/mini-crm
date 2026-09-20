class CustomerRepository:
    def __init__(self,connection):
        self.connection = connection


    def add(self,name,phone,email,company,position,registered_at,notes):
        sql = ''' INSERT INTO customers (
        name,
        phone,
        email,
        company,
        position,
        registered_at,
        notes
        ) 
        VALUES(?,?,?,?,?,?,?)
        '''
        
        cursor = self.connection.cursor()
        cursor.execute(sql,(name,phone,email,company,position,registered_at,notes))

        self.connection.commit()

    def get_all(self):
        sql = "SELECT * FROM customers WHERE is_deleted = 0 "
        cursor = self.connection.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    def get_by_id(self,customer_id):
        sql = "SELECT * FROM customers WHERE id = ? "
        cursor = self.connection.cursor()
        cursor.execute(sql,(customer_id,))
        return cursor.fetchone()


    def update(self,customer_id,name,phone,email,company,position,notes):
        sql = "UPDATE customers SET name=?,phone=?,email=?,company=?,position=?,notes=? WHERE id=?"
        cursor = self.connection.cursor() 
        cursor.execute(sql,(name,phone,email,company,position,notes,customer_id))
        self.connection.commit()

    def delete(self,customer_id):
        sql = "UPDATE customers SET is_deleted = 1 WHERE id =?"
        cursor = self.connection.cursor()
        cursor.execute(sql,(customer_id,))
        self.connection.commit()