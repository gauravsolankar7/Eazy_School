import oracledb
from oracledb import connect

def insertdata(firstname, lastname, email, phoneno, address, doctor, date, time):
    connection = None
    cursor =None
    try:
       # Define your connection credentials
       print("insert data function called")
       username = 'system'
       password = '1234'
       dsn = "localhost:1521/orcl"

       # Connect to the Oracle database
       connection = connect(user=username, password=password, dsn=dsn)
       cursor = connection.cursor()
       print("connection is open and cursor is open")
       # SQL to insert data
       insert_query = "INSERT INTO AHOSPITAL (FIRSTNAME, LASTNAME, EMAIL, PHONENO, ADDRESS, DOCTOR, DATES, TIME) VALUES (:1, :2, :3, :4, :5, :6, :7, :8)"

       # Data to be inserted
       data = (
           firstname, lastname, email, phoneno, address, doctor, date, time)

       cursor.execute(insert_query, data)

       # Commit the transaction
       connection.commit()


    except oracledb.DatabaseError as e:
       print(f"Database error: {e}")
       if connection:
           connection.rollback()
    finally:
    # Close the cursor and connection
      if cursor:
        cursor.close()
      if connection:
         connection.close()
    print("Data inserted and connection closed")