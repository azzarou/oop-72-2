import sqlite3

connect = sqlite3.connect("cinema.db")
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY,
        title TEXT,
        genre TEXT
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        movie_id INTEGER,
        rating INTEGER
    )
""")

cursor.execute("DELETE FROM reviews")
cursor.execute("DELETE FROM users")
cursor.execute("DELETE FROM movies")

cursor.execute("""
    INSERT INTO users (name)
    VALUES
        ('Алиса'),
        ('Бектур'),
        ('Камила'),
        ('Данияр'),
        ('Елена')
""")

cursor.execute("""
    INSERT INTO movies (title, genre)
    VALUES
        ('Начало', 'Фантастика'),
        ('Интерстеллар', 'Фантастика'),
        ('Зеленая миля', 'Драма'),
        ('Джентльмены', 'Боевик'),
        ('Титаник', 'Мелодрама')
""")

cursor.execute("""
    INSERT INTO reviews (user_id, movie_id, rating)
    VALUES
        (1, 1, 10),
        (2, 1, 9),
        (3, 1, 8),
        (1, 2, 10),
        (4, 2, 9),
        (2, 3, 10),
        (5, 3, 9),
        (3, 4, 8),
        (4, 4, 7),
        (5, 4, 9)
""")

connect.commit()

print("1.Пользователь, фильм и оценка:")
cursor.execute("""
    SELECT users.name, movies.title, reviews.rating
    FROM reviews
    JOIN users ON reviews.user_id = users.id
    JOIN movies ON reviews.movie_id = movies.id
""")
for row in cursor.fetchall():
    print(row)

print("2.Все фильмы:")
cursor.execute("""
    SELECT movies.title, reviews.rating
    FROM movies
    LEFT JOIN reviews ON movies.id = reviews.movie_id
""")
for row in cursor.fetchall():
    print(row)

print("3.Оценки:")
cursor.execute("""
    SELECT AVG(rating), MAX(rating), MIN(rating)
    FROM reviews
""")
res = cursor.fetchone()

print("Средняя:", round(res[0], 2))
print("Максимальная:", res[1])
print("Минимальная:", res[2])
connect.close()
