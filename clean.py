import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('scraped_data.csv')
# Example: Remove duplicates
df_cleaned = df.drop_duplicates()


engine = create_engine('mysql://root:1234@connect:3306/DA')

table_name = 'business_data'

df_cleaned.to_sql(table_name, con=engine, if_exists='replace', index=False)
engine.dispose()
