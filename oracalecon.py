import cx_Oracle

conn = cx_Oracle.connect('azhar/redhat@localhost')
cur = conn.cursor()
cur.execute('select * from dept')
for tables in cur:
    print(tables)
