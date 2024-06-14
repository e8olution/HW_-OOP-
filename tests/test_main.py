import pytest
from src.main import Product
from src.main import Category
from unittest.mock import patch




@pytest.fixture
def category_data():
    return Category('Electronics', 'Smartphones',
                    [
                        Product('Iphone','New_1', 99.999, 100),
                        Product('Samsung','New_2', 89.999, 99)
                    ]
                    )
def test_init_category(category_data):
    # Проверка корректности инициализации объектов класса Category
    assert category_data.name == 'Electronics'
    assert category_data.description == 'Smartphones'
    assert category_data.description == 'Smartphones'
    assert len(category_data.products) == 2

    assert category_data.count_uniq_cat == 2
    assert category_data.count_categories == 1

@pytest.fixture
def product_data():
    return (Product('Samsung','A mobile phone with advanced features',999.999, 100)
    )

def test_init_product(product_data):
    assert product_data.name == "Samsung"
    assert product_data.description == "A mobile phone with advanced features"
    assert product_data.price == 999.999
    assert product_data.quantity == 100

product1 = Product("Apple", "Fresh Apple", 10.0, 50)


def test_price(product_data):
    assert product_data._price == 999.999
def test_price_lower_yes(product_data):
    with patch('builtins.input', return_value='y'):
        product_data.price = 99.999
    assert product_data._price == 99.999
def test_price_lower_no(product_data):
    with patch('builtins.input', return_value='n'):
        product_data.price = 99.999
    assert product_data._price == 999.999

def test_price_lower_no(product_data):
    with patch('builtins.input'):
        product_data.price = -99.999
    assert product_data._price == 999.999
def test_price_lower_no(product_data):
    with patch('builtins.input'):
        product_data.price = 0
    assert product_data._price == 999.999