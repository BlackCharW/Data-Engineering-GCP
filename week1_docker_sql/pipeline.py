import os
import pandas as pd
from sqlalchemy import create_engine

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    csv_name = 'output.csv'
    
    os.system(f"wget {url} -O {csv_name}")
    # download the csv
    
    engine = create_engine(f'mysql://{user}:{password}@{host}:{port}/{db}')
    
    df = pd.read_csv(csv_name)
    
    #df.head(n=0).to_sql(name=table_name,con=engine,if_exists='replace')
    
    df.to_sql(name=table_name,con=engine,if_exists='append')
    