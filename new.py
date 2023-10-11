# import psycopg2

# try:
#     conn = psycopg2.connect(host='localhost', database='postgres', user='postgres',password='root')
    
#     cursor = conn.cursor()
#     print("Database connecion was successful")
#     posts = cursor.fetchall()
#     print(posts)
# except Exception as error:
#     print("Connection failed")
#     print("Error;",error)
# import pandas as pd

# from sqlalchemy import create_engine

# eng = create_engine('postgresql://postgres:root@localhost/postgres')

# eng.connect()

# query = """
# SELECT * from persons;
# """

# df = pd.read_sql(query, con=eng)


# print("++++++++++attempted+++++++++")

# print(df)