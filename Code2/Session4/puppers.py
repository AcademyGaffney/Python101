import mysql.connector as MYSQL


class PupperDB:
    def __init__(self, connection):
        # self.Connect = None
        # try:
        self.Connect = MYSQL.connect(user=connection.get('user'),
                                     password=connection.get('pass'),
                                     database=connection.get('db'),
                                     host=connection.get('host'),
                                     auth_plugin='mysql_native_password')
        print('\nConnection to {0} successful.'.format(connection.get('db')))

    # except MYSQL.Error as e:
    #    print(str(e))
    # except:
    #    print("Unknown Error")

    def insert(self, stmt, values):
        try:
            cursor = self.Connect.cursor()
            cursor.execute(stmt.format(*values))
            cursor.close()
        except MYSQL.Error as e:
            self.Connect.rollback()
            print(str(e))
        except:
            self.Connect.rollback()
            print("Unknown error.")
        else:
            self.Connect.commit()
            print('\nInsertion successful')

    def select(self, stmt, values):
        try:
            cursor = self.Connect.cursor()
            cursor.execute(stmt.format(*values))
        except MYSQL.Error as e:
            self.Connect.rollback()
            print(str(e))
        except:
            self.Connect.rollback()
            print("Unknown error.")


def main():
    conn = {'user': 'root', 'pass': 'root', 'db': 'pupperpals', 'host': '127.0.0.1'}
    db = PupperDB(conn)

    print(db.select("Select * from breed", {}))


main()
