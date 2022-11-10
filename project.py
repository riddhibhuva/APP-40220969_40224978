import json
import sqlite3

conn = sqlite3.connect('web_scrapy')
db_json = json.load(open('db.json'))

columns = []
column = []
for data in db_json:
    column = list(data.keys())
    for col in column:
        if col not in columns:
            columns.append(col)

value = []
values = []
for data in db_json:
    for i in columns:
        value.append(str(dict(data).get(i)))
    values.append(list(value))
    value.clear()

create_query = 'create table if not exists Sources (Source_id, Source_name)'
insert_query = 'insert into Sources values (?,?,?)'
c = conn.cursor()
c.execute(create_query)
c.executemany(insert_query, values)
conn.commit()
c.close()