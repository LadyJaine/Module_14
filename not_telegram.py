import sqlite3
import random

connection = sqlite3.connect("not_telegramm.db")
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER)
''')
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users(email)")
# for i in range(10):
#     cursor.execute("INSERT INTO Users(username,email,age,balance) VALUES(?,?,?,?)",(f"username{i+1}", f"example{i+1}@gmail.com", random.randint(10,99), 1000))

# cursor.execute("UPDATE Users SET balance=500 WHERE ID%2=0") #Обновите balance у каждой 2ой записи начиная с 1ой на 500:
#
for i in range(50):
    cursor.execute("DELETE FROM Users  WHERE id%3=0") #Удалите каждую 3ую запись в таблице начиная с 1ой:

cursor.execute("SELECT * FROM Users WHERE age!=60")
users = cursor.fetchall()
for user in users:
    print(user)
connection.commit()
connection.close()

