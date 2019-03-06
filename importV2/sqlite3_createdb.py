import os
import sqlite3

db_filename = 'todd.db'

db_is_new = not os.path.exists(db_filename)
conn = sqlite3.connect(db_filename)

c = conn.cursor()
c.execute('''CREATE TABLE monthtotal
       (sbbh varchar(200),
        datetime      varchar(200),
        zt varchar(200));''')
conn.commit()
conn.close()