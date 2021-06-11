import mysql.connector

class JenisMakanan:
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

    def getJenisMakananByNama(self, namaMakanan):
        value = (namaMakanan.capitalize())
        query = "SELECT * FROM jenis_makanan WHERE nama_jenis_makanan= " + value
        print(value)
        self.cursor.execute(query)
        data = self.cursor.fetchone()
        print(data)

coba = JenisMakanan()
coba.getJenisMakananByNama("Buah")