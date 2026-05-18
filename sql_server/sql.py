import typing_extensions
from sqlalchemy import create_engine
import urllib

# Get engine para rodar localmente
def get_engine():
    server = 'localhost' 
    database = 'master'
    driver = 'ODBC Driver 17 for SQL Server'
    
    params = urllib.parse.quote_plus(
        f"DRIVER={{{driver}}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"Trusted_Connection=yes;"
    )
    
    return create_engine(
        f"mssql+pyodbc:///?odbc_connect={params}",
        fast_executemany=True
    )

# Func para Inserir dados no SQL Server
def inserir_dados(df , tabela, engine):

    df.to_sql(
        name=tabela,
        con=engine,
        if_exists='append',
        Index=False,
        chunksize=20000
    )


def if_exists():
    print("Caique é gayy")