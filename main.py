import psycopg2
import requests
import keyring
import json
import zlib

# To Secure you credentials use the code below and run in your environment once.
# after that use "keyring.get_password("postgre_password", "snehil_admin")"
# instead of typing your password thereby not exposing the password.
keyring.set_password("postgre_password", "snehil_admin", "Sv@7860507207")


print("=====================================Connecting To PostGre SQL=========================================")


try:
    conn = psycopg2.connect(
       database="api_sample", user='postgres', password=keyring.get_password("postgre_password", "snehil_admin"), \
       host='127.0.0.1', port= '5432'
    )
    cursor = conn.cursor()                                 #Creating a cursor object using the cursor() method
    cursor.execute("select version()")                     #Executing an SQL function using the execute() method
    data = cursor.fetchone()                               # Fetch a single row using fetchone() method.
    print("Connection established to: ", data)

except:
    print("Database Connection Error")


# -------------------------------------------GETTING API DATA----------------------------------------------


print("===================================Getting Data From theDogAPI=====================================")
response = requests.get("https://api.thedogapi.com/v1/breeds")
response_json_format = response.json()


# -----------------------------------CREATE SQL STATEMENT AND TABLE-----------------------------------------


print(".....Analyzing the Data and Creating Schema and Table.....")


def schema_analyzation_table_creation():
    try:
        create_statement = "CREATE TABLE dogs ( "
        sql_statement = ""
        column_names = {}
        column_names = set(response_json_format[1])                                      #SETTING BASE COLUMNS

        for i in response_json_format:
            column_names.update(set(i))                                            #

        for j in column_names:
            sql_statement = sql_statement + j + " VARCHAR,"

        sql = (create_statement + sql_statement[0:-1] + " )")

        cursor.execute("DROP TABLE IF EXISTS DOGS")             #Doping EMPLOYEE table if already exists.
        cursor.execute(sql)                                     #Creating table as per requirement
        conn.commit()

    except:
        print(".....Issue in Creating Schema and Table.....")
    print(".....Table created successfully.....")


# -------------------------------------------INSERT AND ALTER TABLE-----------------------------------------


print(".....Constructing SQL INSERT Statement and Inserting rows to the Table.....")


def data_ingestion():
    try:
        insert = ""
        values = ""

        for l in response_json_format:
            for key, value in l.items():
               insert = insert + str(key) + ", "
               values = values + "'" + (str(value).replace("'", "\"")) + "'" + ", "
            sql_insert_satatement = "INSERT INTO dogs ( " + insert[0:-2] + " ) VALUES ( " + values[0:-2] + ")"
            cursor.execute(sql_insert_satatement)                          # Creating table as per requirement
            conn.commit()
            insert = ""
            values = ""
            sql_insert_satatement = ""

    except:
        print(".............................Issue in Schema Creation/Row Insertion..................................")

    print("INGESTION OF DATA IS COMPLETE..........NOW GO AND HAVE A BEER")


# --------------------------------------------#Closing the connection---------------------------------------


def close_postgre_connection():
    conn.close()
    print("=====================================Connection is Closed.=========================================")
# Connection established to: (
#    'PostgreSQL 11.5, compiled by Visual C++ build 1914, 64-bit',
# )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    schema_analyzation_table_creation()
    data_ingestion()
    close_postgre_connection
