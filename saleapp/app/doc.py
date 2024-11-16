from app import db, app
from app.models import Category, Product


def get_categories():
    return Category.query.order_by("id").all()


def get_products(category_id=None, kw=None, page=1):
    query = Product.query

    if category_id:
        query = query.filter(Product.category_id == category_id)

    if kw:
        query = query.filter(Product.name.contains(kw))

    start = (page - 1) * app.config["PAGE_SIZE"]
    query = query.slice(start, page * app.config["PAGE_SIZE"])

    return query.all()


def total_products():
    return Product.query.count()
