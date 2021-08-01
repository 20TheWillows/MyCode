import pyodbc
import numpy as np
import pandas as pd
import uuid

def connect():
    try:
        conn = pyodbc.connect(r"""
                            Driver={SQL Server};
                            Server=SIMONLAPTOP\SQLEXPRESS;
                            Database=SimonsDatabase;
                            Trusted_Connection=yes;
                            """)
        return conn
    except:
        raise ConnectionError("Error connecting to SQL Server database")

def database_contents_as_dataframe(conn):
    try:
        sql_query = pd.read_sql_query('SELECT * FROM SimonsDatabase.dbo.Students',conn)
        return sql_query
    except:
         raise ConnectionError("Error connecting to SQL Server database")

def mycondition(row):
    if row['Age'] > 30 or row['Surname'].lower() == 'robson':
        return False
    else:
        return True

if __name__ == "__main__":
    try:
        db_connection = connect()
        # Get user info to insert into db
        while True:
            df = database_contents_as_dataframe(db_connection)
            print(df)
            user_first_name = input("Enter first name:")
            if user_first_name.lower() == "q":
                break
            user_surname = input("Enter surname:")
            if user_surname.lower() == "q":
                break
            user_age = input("Enter your age:")
            # Got data, now indert into database
            cursor = db_connection.cursor()
            sql_string = "INSERT INTO Students VALUES('%s','%s', '%s', '%s')" % (uuid.uuid4(), user_first_name, user_surname, user_age)
            cursor.execute(sql_string)
            db_connection.commit()
    except Exception as error:
        print("Exception: " + str(error))
    finally:
        # Add a column to df
        df['Bool'] = df.apply(mycondition, axis=1)
        print(df)
    db_connection.close()

