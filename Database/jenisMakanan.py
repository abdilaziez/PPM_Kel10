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

    def getIdJenisMakananByNama(self, namaMakanan):
        value = namaMakanan.capitalize()
        query = "SELECT ID_jenis_makanan FROM jenis_makanan WHERE nama_jenis_makanan='"+ value + "'"
        self.cursor.execute(query)
        data = self.cursor.fetchone()
        if self.cursor.rowcount != -1:
            return data[0]
        else:
            self.simpanJenisMakanan(namaMakanan)
            self.getIdJenisMakananByNama(namaMakanan)

    def simpanJenisMakanan(self, namaMakanan):
        value = namaMakanan.capitalize()
        query = "INSERT INTO `jenis_makanan`(`nama_jenis_makanan`) VALUES ('" + value + "')"
        self.cursor.execute(query)
        self.con.commit()
        return self.cursor.rowcount

    def getJenisMakanan(self):
        query = "SELECT * FROM jenis_makanan"
        self.cursor.execute(query)
        return self.cursor.fetchall()
