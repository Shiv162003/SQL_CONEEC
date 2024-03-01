#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector
import pandas as pd


# In[2]:


host = 'localhost'
user = 'root'
password = 'shan12345'
database='imdb'


connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)


cursor = connection.cursor()


show_tables_query = 'SHOW TABLES'
cursor.execute(show_tables_query)


tables = cursor.fetchall()

#dictionary to store DataFrames
dataframes = {}

# Iterate through each table and create a DataFrame
for table in tables:
    table_name = table[0]
    query = f'SELECT * FROM {table_name}'
    dataframe = pd.read_sql(query, connection)
    dataframes[table_name] = dataframe

# Display the DataFrames
for table_name, dataframe in dataframes.items():
    print(f" '{table_name}':")
    print(dataframe.head())


# In[3]:


print(f"\nDataFrame for table 'actors':")
print(dataframe.head())


# In[ ]:




