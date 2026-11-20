import sqlite3

connect = sqlite3.connect("store.db")
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name VARCHAR(30) NOT NULL,
        price FLOAT NOT NULL,
        quantity INTEGER NOT NULL
    )
""")
connect.commit()

def create_product(name, price, quantity):
    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity),
    )
    connect.commit()
    print("Продукт создан")

def read_products():
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()
    print("Все товары:", data)
    return data

def update_product(id, price):
    cursor.execute(
        "UPDATE products SET price = ? WHERE id = ?",
        (price, id),
    )
    connect.commit()
    print("Прайс обновлен")

def delete_product(id):
    cursor.execute(
        "DELETE FROM products WHERE id = ?",
        (id,),
    )
    connect.commit()
    print("Товар удален")

create_product("Клавиатура", 2500, 10)
read_products()
update_product(1, 2200)
read_products()
delete_product(1)
read_products()
connect.close()