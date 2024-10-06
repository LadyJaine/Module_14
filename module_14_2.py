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
cursor.execute("DELETE FROM Users  WHERE id=6") #Удалите из базы данных not_telegram.db запись с id = 6.
users = cursor.fetchall()
for user in users:
    print(user)
cursor.execute("SELECT COUNT(username) FROM Users") #Подсчёт кол-ва всех пользователей
total_users = cursor.fetchone()[0]
print(total_users)
cursor.execute("SELECT SUM(balance) FROM Users") #Подсчёт суммы всех балансов
total_balance = cursor.fetchone()[0]
print(total_balance)

connection.commit()
connection.close()
