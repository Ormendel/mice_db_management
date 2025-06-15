import pymysql

conn = pymysql.connect(
    host='10.0.0.22',
    user='root',
    password='ORchen3131@mendelzusman',
    port=3131,
    database='mice'
)

with conn.cursor() as cursor:
    cursor.execute("SHOW DATABASES;")
    for db in cursor.fetchall():
        print(db)

    cursor.execute("SELECT * FROM breeds;")
    for row in cursor.fetchall():
        print(row)
print("Connected successfully! woohoo!")
conn.close()
