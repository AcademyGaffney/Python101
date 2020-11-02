import mysql.connector as MYSQL

class PupperPalsDAO:
    def __init__(self):
        self.connect = MYSQL.connect(user = "root",
                                     password = "root",
                                     host = "127.0.0.1",
                                     database = "PupperPals")

    def selectAllPuppers(self):
        pStmt = "Select * from pupper"
        cursor = self.connect.cursor()
        cursor.execute(pStmt)
        for row in cursor:
            print(row)


def main():
    dao = PupperPalsDAO()
    dao.selectAllPuppers()

main()
