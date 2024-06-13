import pytest
from modules.common.database import Database
from sqlite3 import OperationalError, IntegrityError
import datetime


@pytest.mark.database
def test_database_connection(db_connection): # fixture using
    db_connection.test_connection()


@pytest.mark.database
def test_check_all_users(db_connection):
    users = db_connection.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii(db_connection):
    user = db_connection.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update(db_connection):
    db_connection.update_product_qnt_by_id(1, 25)
    water_qnt = db_connection.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25 # Перевірити, що після оновлення даних кількість товару з унікальним номером 1 дорівнює 25


@pytest.mark.database
def test_product_insert(db_connection):
    db_connection.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db_connection.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete(db_connection):
    db_connection.insert_product(99, 'тестові', 'дані', 999) # створити тестові дані, створивши, продукт в таблиці products зі значеннями параметрів product_id = 99, name = тестові, description = дані, qnt = 999
    db_connection.delete_product_by_id(99) # видалити дані з таблички products зі значенням параметра product_id = 99
    qnt = db_connection.select_product_qnt_by_id(99)

    assert len(qnt) == 0 # Перевірити, що кількість рядків, що було знайдено дорівнює 0


@pytest.mark.database
def test_detailed_orders(db_connection):
    orders = db_connection.get_detailed_orders()
    print("Замовлення", orders)

    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check struture of data
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'


@pytest.mark.database_hw                                 # new mark for HomeWork tests 
def test_adding_invalid_string_id_for_customer(db_connection):
    with pytest.raises(OperationalError):
        db_connection.insert_new_customer('чотири', 'Oksana', 'бул.Правди 16', 'Lviv', 'A324', 'Ukraine')
    cust = db_connection.get_user_by_id(4)
    
    # check that "Error: no such column: чотири" is shown if try to enter id as a string
    assert len(cust) == 0
    

@pytest.mark.database_hw
def test_adding_customer_with_float_id(db_connection):
    with pytest.raises(IntegrityError):
        db_connection.insert_new_customer(3.5, 'Oksana', 'бул.Правди 16', 'Lviv', 'A324', 'Ukraine')
    cust = db_connection.get_user_by_id(3.5)

    # check that "Error: datatype mismatch" is shown if try to enter id as a float
    assert len(cust) == 0
    

@pytest.mark.database_hw
def test_nsert_replace_new_order_with_valid_data(db_connection):
    valid_date = datetime.datetime.now()  # date format
    db_connection.insert_replace_new_order(2, 2, 3, valid_date)
    order = db_connection.get_orders_by_id(2)
    print("New order № 2", order)

    # check that new order with valid new date is created
    assert len(order) > 0  
    assert order[0][3] != '2024-06-09'


@pytest.mark.database_hw
def test_detailed_orders_product_name(db_connection):
    orders = db_connection.get_detailed_orders()
    print("All orders:", orders)

    # check that in 2nd order product name is молоко
    assert orders[1][2] == 'молоко'


@pytest.mark.database_hw
def test_update_adress_for_customer_by_name_and_country(db_connection):
    db_connection.update_adress_for_customer_by_name_and_country('Sergii', 'Ukraine', 'Akademika Hlushkova 23')
    new_address = db_connection.get_user_address_by_name_and_country('Sergii', 'Ukraine')

    # check that new adress of customer Sergii from Ukraine is Akademika Hlushkova 23
    assert new_address[0][0] == 'Akademika Hlushkova 23'
