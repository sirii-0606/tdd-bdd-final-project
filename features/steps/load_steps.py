"""
Load Steps for BDD
"""
from decimal import Decimal
from behave import given  # pylint: disable=no-name-in-module
from service.models import Product, Category


@given("the following products")
def step_impl(context):
    """Load the database with new Products"""
    # List all of the products and delete them one by one
    Product.remove_all()
    for row in context.table:
        product = Product()
        product.name = row["name"]
        product.description = row["description"]
        product.price = Decimal(row["price"])
        product.available = row["available"] in ["True", "true", "1"]
        product.category = getattr(Category, row["category"].upper())
        product.create()
