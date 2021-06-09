import mysql.connector

class AkunAdmin:
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
        
    def coba():
        print("error")

    # def update(self, code, value):
    #     try:
    #         con = mysql.connector.connect(
    #             host="localhost",
    #             user="root",
    #             password="",
    #             database = "porsi_makanan"
    #         )
    #         cursor = con.cursor();
    #         cursor.execute(code, value)
    #         con.commit()
    #     except mysql.connector.Error as e:
    #         print("Failed connect to database in MySQL: {}".format(e))

    # def read(self, code, value=[]):
    #     try:
    #         con = mysql.connector.connect(
    #             host="localhost",
    #             user="root",
    #             password="",
    #             database = "porsi_makanan"
    #         )
    #         cursor = con.cursor();
    #         cursor.execute(code, value)
    #         data = []
    #         for i in cursor:
    #             data.append(i)
    #         return data
    #     except mysql.connector.Error as e:
    #         print("Failed connect to database in MySQL: {}".format(e))