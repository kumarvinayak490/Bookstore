import psycopg2

def create_table():
    conn= psycopg2.connect("dbname='database1' user='postgres' password='mother@143' host='localhost' port='5432' ")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(Item TEXT, Quantity INTEGER, Price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='mother@143' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item,quantity,price))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='mother@143' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='mother@143' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute('DELETE FROM store WHERE Item=%s',(item,))
    conn.commit()
    conn.close()

def update(item, price , quantity):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='mother@143' host='localhost' port='5432'")
    cur= conn.cursor()
    cur.execute('UPDATE store SET price=%s, quantity=%s WHERE Item=%s',(price,quantity,item))
    conn.commit()
    conn.close()

create_table()
update('ball',30,40)

print(view())








