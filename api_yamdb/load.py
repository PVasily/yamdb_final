import csv
import sqlite3

con = sqlite3.connect("db.sqlite3")
cur = con.cursor()
with open('static/data/users.csv', 'r', encoding='utf-8') as fin:
    dr = csv.DictReader(fin)
    to_db = [
        (
            i['id'],
            i['username'],
            i['email'],
            i['role'],
            i['bio'],
            i['first_name'],
            i['last_name'])
        for i in dr
    ]
cur.executemany(
    """
    INSERT INTO reviews_user
    (
        id,
        username,
        email,
        role,
        bio,
        first_name,
        last_name,
        password,
        is_superuser,
        is_staff,
        is_active,
        date_joined
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, 0, 0, 0, 1, 0);""", to_db)
con.commit()
con.close()
