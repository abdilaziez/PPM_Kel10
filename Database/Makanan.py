import mysql.connector

class Makanan:
    def __init__(self):
        try:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database = "porsi_makanan"
            )
            self.cursor = con.cursor()
        except mysql.connector.Error as e:
            self.error = "Failed connect to database in MySQL: {}".format(e)