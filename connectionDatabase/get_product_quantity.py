import psycopg2

def get_quantity(type,name,quantity):

    conn = psycopg2.connect("dbname=postgres user=postgres password=1221")

    cur = conn.cursor()

    cur.execute(f"select quantity from products where type='{type}' and name='{name}';")

    rows = cur.fetchall()
    soni = rows[0][0]

    if soni >= quantity:
        cur.execute(f"update products set quantity=(quantity - {quantity}) where type='{type}' and name='{name}';")
        cur.execute(f"select price from products where type='{type}' and name='{name}';")
        res = cur.fetchall()
        res = res[0][0] * quantity
        return res
    elif soni < quantity:
        return "Korzinkada yetarli mahsulot yoq"

    conn.commit()

    cur.close()
    conn.close()



# print(get_quantity('food', 'rice', 10))