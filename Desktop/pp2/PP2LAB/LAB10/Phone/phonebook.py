import psycopg2
import csv

# 连接数据库
def connect():
    return psycopg2.connect(
        host="localhost",
        database="Phone",       # 你的数据库名
        user="mariyaerzhan",    # 数据库用户名
        password="123456"       # 数据库密码
    )

# 创建表
def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            phone VARCHAR(20),
            email VARCHAR(100)
        );
    ''')
    conn.commit()
    cur.close()
    conn.close()
    print("Table created successfully.")

# 从 CSV 导入
def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute("""
                INSERT INTO phonebook (first_name, last_name, phone, email)
                VALUES (%s, %s, %s, %s)
            """, (row['first_name'], row['last_name'], row['phone'], row['email']))
    conn.commit()
    cur.close()
    conn.close()
    print("Data inserted from CSV.")

# 从输入插入
def insert_from_input():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO phonebook (first_name, last_name, phone, email)
        VALUES (%s, %s, %s, %s)
    """, (first_name, last_name, phone, email))
    conn.commit()
    cur.close()
    conn.close()
    print("User inserted.")

# 更新用户
def update_user():
    name = input("Enter first name to update: ")
    new_phone = input("New phone (Enter to skip): ")
    new_email = input("New email (Enter to skip): ")
    conn = connect()
    cur = conn.cursor()
    if new_phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s", (new_phone, name))
    if new_email:
        cur.execute("UPDATE phonebook SET email = %s WHERE first_name = %s", (new_email, name))
    conn.commit()
    cur.close()
    conn.close()
    print("User updated.")

# 查询用户
def query_user():
    name = input("Enter first name to search (Enter to show all): ")
    conn = connect()
    cur = conn.cursor()
    if name:
        cur.execute("SELECT * FROM phonebook WHERE first_name = %s", (name,))
    else:
        cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

# 删除用户
def delete_user():
    name = input("Enter first name to delete: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
    conn.commit()
    cur.close()
    conn.close()
    print("User deleted.")

# 菜单
def menu():
    while True:
        print("\nPHONEBOOK MENU")
        print("1. Create Table")
        print("2. Insert from CSV")
        print("3. Insert from Input")
        print("4. Update User")
        print("5. Query User")
        print("6. Delete User")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_table()
        elif choice == "2":
            insert_from_csv("data.csv")
        elif choice == "3":
            insert_from_input()
        elif choice == "4":
            update_user()
        elif choice == "5":
            query_user()
        elif choice == "6":
            delete_user()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
