import mysql.connector

class AkunAdmin:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database = "porsi_makanan"
            )
            self.cursor = self.con.cursor()
        except mysql.connector.Error as e:
            self.error = "Failed connect to database in MySQL: {}".format(e)
        
    def getUserByUsernameAndPassword(self, username, password):
        query = "SELECT * FROM akun_admin WHERE username= %s AND password= %s"
        value = (username, password)
        self.cursor.execute(query, value)
        self.cursor.fetchone()
        return self.cursor.rowcount