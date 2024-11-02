from app import db
from app.models import Category, Product

def get_categories():
    return Category.query.order_by("id").all()


def get_products(category_id=None, kw=None):
    query = Product.query

    if category_id:
        query = query.filter(Product.category_id == category_id)

    if kw:
        query = query.filter(Product.name.contains(kw))

    return query.all()
