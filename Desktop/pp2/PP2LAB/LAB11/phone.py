import psycopg2
import csv

# 连接数据库
def connect():
    return psycopg2.connect(
        host="localhost",
        database="PhoneBook",       # 你的数据库名
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

def search_by_pattern():
    pattern = input("请输入关键词（名字/姓氏/电话）: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

def insert_or_update_user():
    name = input("名字: ")
    surname = input("姓氏: ")
    phone = input("电话: ")
    email = input("邮箱: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL insert_or_update_user(%s, %s, %s, %s)", (name, surname, phone, email))
    conn.commit()
    cur.close()
    conn.close()
    print("插入或更新完成。")

def insert_many_users():
    n = int(input("输入要插入用户数量: "))
    names = []
    phones = []
    for _ in range(n):
        names.append(input("名字: "))
        phones.append(input("电话: "))
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL insert_many_users(%s, %s)", (names, phones))
    result = cur.fetchone()
    print("以下数据无效:", result[0])
    conn.commit()
    cur.close()
    conn.close()

def get_paginated_users():
    limit = int(input("每页显示多少条: "))
    offset = int(input("跳过多少条: "))
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_users(%s, %s)", (limit, offset))
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

def delete_user_by_name_or_phone():
    name = input("名字（可选）: ") or None
    phone = input("电话（可选）: ") or None
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL delete_user_by_name_or_phone(%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("用户删除完成（如果存在）。")


# 菜单
def menu():
    while True:
        print("Phonebook Menu")
        print("1. Create table")
        print("2. Insert data from CSV")
        print("3. Insert data from input")
        print("4. Update user")
        print("5. Query user")
        print("6. Delete user")
        print("7. Fuzzy search user (Function)")
        print("8. Insert or update user (Stored Procedure)")
        print("9. Insert multiple users (Stored Procedure + Format Validation)")
        print("10. Paginated query (Function)")
        print("11. Delete user by name or phone (Stored Procedure)")
        print("0. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            create_table()
        elif choice == "2":
            insert_from_csv("/Users/mariyaerzhan/Desktop/pp2/PP2LAB/LAB11/data.csv")
        elif choice == "3":
            insert_from_input()
        elif choice == "4":
            update_user()
        elif choice == "5":
            query_user()
        elif choice == "6":
            delete_user()
        elif choice == "7":
            search_by_pattern()
        elif choice == "8":
            insert_or_update_user()
        elif choice == "9":
            insert_many_users()
        elif choice == "10":
            get_paginated_users()
        elif choice == "11":
            delete_user_by_name_or_phone()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    menu()
