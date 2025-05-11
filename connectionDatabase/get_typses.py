import psycopg2

def get_type():
    conn = psycopg2.connect("dbname=postgres user=postgres password=1221")

    cur = conn.cursor()

    cur.execute("select distinct type from products;")

    rows = cur.fetchall()

    conn.commit()

    cur.close()
    conn.close()

    return rows