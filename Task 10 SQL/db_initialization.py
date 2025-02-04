import pyodbc

connection = pyodbc.connect('DRIVER={SQLite3 ODBC Driver};'
                            'Direct=True;'
                            'Database=test.db;'
                            'String Types=Unicode')

cursor = connection.cursor()
cursor.execute('CREATE TABLE News (text text, city text, date text)')
cursor.execute('CREATE TABLE Advertisement (text text, expiration_date text)')
cursor.execute('CREATE TABLE MyPost (user_name text, text text, date_of_post text)')

connection.commit()

cursor.close()
connection.close()