import pandas as pd
import glob
import pyodbc
import os

# Define the path of the CSV files here
path = r'C:\Users\rocks\Documents\Stocks\Archive\2023'
all_files = glob.glob(os.path.join(path, "*.csv"))

data = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)
df = pd.DataFrame(data)
df = df.fillna(value=0)

print(df)

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=WorkPC;'
                      'Database=StockDB;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

for row in df.itertuples():
    cursor.execute('''
                INSERT INTO source.bhavcopysrc (SYMBOL, SERIES, [OPEN], HIGH,LOW,[CLOSE],LAST,PREVCLOSE,TOTTRDQTY,TOTTRDVAL,TIMESTAMP,TOTALTRADES,ISIN)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
                ''',
                row.SYMBOL,
                row.SERIES,
                row.OPEN,
                row.HIGH,
                row.LOW,
                row.CLOSE,
                row.LAST,
                row.PREVCLOSE,
                row.TOTTRDQTY,
                row.TOTTRDVAL,
                row.TIMESTAMP,
                row.TOTALTRADES,
                row.ISIN
                )
conn.commit()

cursor.close()