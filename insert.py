import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import os

conn_string = 'postgresql://postgres:DSW123@43.204.222.177:5432/temp'
db_alchamey = create_engine(conn_string)
conn_alchamey = db_alchamey.connect()

conn = psycopg2.connect(conn_string)
cursor_pg = conn.cursor()

def read_frm_csv(csv_path):
    data = pd.read_csv(csv_path, sep=',')   
    print(data.columns)
    df = pd.DataFrame(data, columns=data.columns)
    return df

def insert_df(df,table_name):
    print(table_name)
    df.to_sql(table_name, con=conn_alchamey, if_exists='replace', index=False)
    conn.commit()

if __name__ == '__main__':
    root_path = '' #Insert the root folder
    files_list = os.listdir(root_path) #list of files
    print(files_list)
    for file in files_list:
        df = read_frm_csv(os.path.join(root_path,file))
        insert_df(df,file[:-4])