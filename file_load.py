import sqlalchemy
import pandas as pd

user = 'user'
pwd = 'pwd'
server ='server'
port = '5432'
db = 'db'

engine = sqlalchemy.create_engine(f'postgresql://{user}:{pwd}@{server}:{port}/{db}')

readPath = #enter the readpath of the document you are adding
df = pd.read_excel(readPath, dtype=str)
df.to_sql(#enterthenameofthetableyouwant, con=engine, if_exists='replace', index=False)