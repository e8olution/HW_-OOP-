import pytest
from src.main import Product
from src.main import Category
from src.main import Smartphone
from src.main import Grass
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
    assert category_data.name_category == 'Electronics'
    assert category_data.description_category == 'Smartphones'
    assert category_data.description_category == 'Smartphones'
    assert len(category_data.products) == 2
    assert category_data.count_uniq_cat == 2
    assert category_data.count_categories == 1

@pytest.fixture
def product_data():
    return (Product('Samsung','A mobile phone with advanced features',999.999, 100)
    )

def test_init_product(product_data):
    assert product_data.name_product == "Samsung"
    assert product_data.description_product == "A mobile phone with advanced features"
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

def test_price_neagtive(product_data):
    with patch('builtins.input'):
        product_data.price = -99.999
    assert product_data._price == 999.999

def test_price_zero(product_data):
    with patch('builtins.input'):
        product_data.price = 0
    assert product_data._price == 999.999

def test_add_valid_product(category_data, product_data):
    category_data.add_product(product_data)
    assert product_data in category_data._Category__products

def test_add_valid_smartphone(category_data):
    smartphone = Smartphone("Iphone", "Смартфон Apple", 99.999, 10, "A14", "14 Pro", "256GB", "Black")
    category_data.add_product(smartphone)
    assert smartphone in category_data._Category__products

def test_add_valid_grass(category_data):
    grass = Grass("Газонная трава", "Для дачи", 50, 20, "Россия", "2 недели", "Зеленый")
    category_data.add_product(grass)
    assert grass in category_data._Category__products

def test_add_invalid_object(category_data):
    with pytest.raises(TypeError):
        category_data.add_product("не продукт")

def test_category_length(category_data):
    assert len(category_data) == sum(product.quantity for product in category_data._Category__products)

def test_category_str(category_data):
    expected_str = f'{category_data.description_category}, количество продуктов: {len(category_data._Category__products)} шт.'
    assert str(category_data) == expected_str

def test_products_format(category_data):
    expected_format = [f'{product.name_product}, {product.price} руб. Остаток: {product.quantity} шт.' for product in category_data._Category__products]
    assert category_data.products == expected_format