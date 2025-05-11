import psycopg2

def get_products(type):
    conn = psycopg2.connect("dbname=postgres user=postgres password=1221")

    cur = conn.cursor()

    cur.execute(f"select name from products where type='{type}';")

    rows = cur.fetchall()

    conn.commit()

    cur.close()
    conn.close()

    return rows
