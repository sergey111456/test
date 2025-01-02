import sqlite3
import re

# Підключення до бази даних
def connect_db():
    return sqlite3.connect('users.db')

# Створення таблиці, якщо вона не існує
def create_table():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

# Реєстрація нового користувача
def register_user(username, password):
    with connect_db() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            print("✅ Реєстрація пройшла успішно!")
        except sqlite3.IntegrityError:
            print("❌ Користувач з таким ім'ям вже існує. Спробуйте інше ім'я.")

# Перевірка, чи існує користувач
def user_exists(username):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        return cursor.fetchone() is not None

# Валідація імені користувача
def validate_username(username):
    if len(username) < 3:
        print("❌ Ім'я користувача повинно містити щонайменше 3 символи.")
        return False
    return True

# Валідація пароля
def validate_password(password):
    if len(password) < 6:
        print("❌ Пароль повинен містити щонайменше 6 символів.")
        return False
    if not re.search("[a-z]", password):
        print("❌ Пароль повинен містити хоча б одну малу літеру.")
        return False
    if not re.search("[A-Z]", password):
        print("❌ Пароль повинен містити хоча б одну велику літеру.")
        return False
    if not re.search("[0-9]", password):
        print("❌ Пароль повинен містити хоча б одну цифру.")
        return False
    return True
# Перегляд зареєстрованих користувачів
def view_users():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT username FROM users')
        users = cursor.fetchall()

        if not users:
            print("❌ Немає зареєстрованих користувачів.")
        else:
            print("👥 Зареєстровані користувачі:")
            for user in users:
                print(f" - {user[0]}")

# Головна функція
def main():
    create_table()  # Створюємо таблицю при запуску програми

    while True:
        print("\n🌟 Ласкаво просимо до гри!")
        print("1. Реєстрація")
        print("2. Перегляд зареєстрованих користувачів")
        print("3. Вихід")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            username = input("🔑 Введіть ім'я користувача: ")
            if validate_username(username) and not user_exists(username):
                password = input("🔒 Введіть пароль: ")
                if validate_password(password):
                    register_user(username, password)

        elif choice == '2':
            view_users()

        elif choice == '3':
            print("👋 Дякуємо за використання програми!")
            break

        else:
            print("❌ Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()