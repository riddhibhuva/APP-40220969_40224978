import json
import sqlite3

# conn = sqlite3.connect('news.db')
# db_json = json.load(open('db.json'))
#
# columns = []
# column = []
# for data in db_json:
#     column = list(data.keys())
#     for col in column:
#         if col not in columns:
#             columns.append(col)
#
# value = []
# values = []
# for data in db_json:
#     for i in columns:
#         value.append(str(dict(data).get(i)))
#     values.append(list(value))
#     value.clear()
#
# create_query = 'create table if not exists Sources (Source_id, Source_name)'
# insert_query = 'insert into Sources values (?,?)'
# c = conn.cursor()
# c.execute(create_query)
# c.executemany(insert_query, values)
# conn.commit()
# c.close()

connection = sqlite3.connect('news.db')
cursor = connection.cursor()

print(cursor.fetchall())
# cursor.execute('Create Table Movie (id varchar(20), title varchar(20), year int, score int, \
#     score_average int, type varchar(20), tmdbid varchar(20))')

# traffic = response.json()['search']
# #print(traffic)
# columns = ['id', 'title', 'year', 'score', \
#     'score_average', 'type', 'tmdbid']
# for row in traffic:
#     keys= tuple(row[c] for c in columns)
#     cursor.execute('insert into Movie values(?,?,?,?,?,?,?)',keys)

connection.commit()
connection.close()