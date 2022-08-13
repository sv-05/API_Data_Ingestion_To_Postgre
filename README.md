# API_Data_Ingestion_To_Postgre


#OVERVIEW
In this project, it is shown how Data can be extracted from an API endpoint and the process is automated using 
Python Programming Language to give data a structure and then Ingest the data to a Relational Database like Postgre SQL.


#Details About The Methods And Variables Used

=> "keyring.set_password()" - This belongs to the 'keyword' library of python used to hide and save passwords and
                              other similar things like connection strings.
                              You have to run this first in your environment and then simply call your password
                              using 'keyring.get_password()' method.
                              Refer link - https://theautomatic.net/2020/04/28/how-to-hide-a-password-in-a-python-script/                              
                              

=> "requests.get()" - A famous method from library 'requests' which extracts the data from any API endpoint.


=> "schema_analyzation_table_creation()" - In this method, automation runs which first analyse each row of data and learns
                                           the structure/schema of incoming data in a set data structure and finally a 
                                           consolidated table is created.
                                           

=> "data_ingestion()" - Now that we have a schema ready for the table, comes the part where data is ingested in the table.


=> "close_postgre_connection()" - It is always recommended to close the database connection after work is done.
