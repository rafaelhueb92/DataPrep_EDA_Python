import pandas as pd
import sqlite3 as sql

print('Running query')
conn = sql.connect('./Data/maven.db')

courses = pd.read_sql_query("SELECT * FROM courses",conn)

print(courses,courses.shape)

