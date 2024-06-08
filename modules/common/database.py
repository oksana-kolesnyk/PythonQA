import sqlite3


class Database():

    def __init__(self): # конструктор, в якому ініціалізовані два атрибути об’єкта
        self.connection = sqlite3.connect(r'/Users/ksena/PythonQA/PythonQA' + r'/become_qa_auto.db') # об’єкт, який реалізує з'єднання з базою даних
        self.cursor = self.connection.cursor()

    def test_connection(self): # Результатом виконання методу є виведена в термінал версія бази даних
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")
    
    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit() # Метод має змінити кількість товару за вказаним в парметрі product_id унікальним значенням в таблиці products на значення вказаного в параметрі qnt

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record # Метод має повернути кількість товару за вказаним в парметрі product_id унікальним значенням із таблиці products
    
    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit() # Метод має вставити, або замінити дані в таблиці products для колонок id, name, description, quantity. Дані взяти з параметрів product_id, name, description, qnt
    
    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit() # Метод має видалити товар за вказаним в парметрі product_id унікальним значенням із таблиці products

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
                products.description, orders.order_date \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    # Використовуючи команду JOIN та таблиці orders, customers, products, повернути із таблиці orders наступну інформацію у відповідному порядку: унікальний номер замовлення, ім’я покупця, ім’я замовленого продукту, опис замовленого продукту, дату замовлення
