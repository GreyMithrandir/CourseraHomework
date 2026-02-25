import sqlalchemy
import pandas as pd

user = #enter user info
pwd = #enter password
server #enter server info
port = '5432'
db = #enter database info

engine = sqlalchemy.create_engine(f'postgresql://{user}:{pwd}@{server}:{port}/{db}')

readPath = #enter the readpath of the document you are adding
df = pd.read_excel(readPath, dtype=str)
df.to_sql(#enterthenameofthetableyouwant, con=engine, if_exists='replace', index=False)