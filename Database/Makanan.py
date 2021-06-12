import mysql.connector

class Makanan:
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

    def simpanMakanan(self, value):
        query = "INSERT INTO `makanan`(`nama_makanan`, `tipe_makanan`, `massa_dewasa`, `massa_bayi`, `massa_anak_4_10_tahun`, `massa_anak_11_18_tahun`) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(query, value)
        self.con.commit()
        return self.cursor.rowcount

    def getMakananByTipe(self, tipe):
        query = "SELECT * FROM makanan WHERE tipe_makanan='" + str(tipe) + "'"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def getMakanan(self):
        query = "SELECT * FROM makanan "
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        for index in range(len(data)):
            data[index] = list(data[index])
        return data


    def getMakananByNama(self, namaMakanan):
        query = "SELECT * FROM makanan WHERE nama_makanan='" + str(namaMakanan) + "'"
        self.cursor.execute(query)
        return list(self.cursor.fetchone())