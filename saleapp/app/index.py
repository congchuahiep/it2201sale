import math

from flask import render_template, request
import doc
from app import app


@app.route("/")
def index():
    categories = doc.get_categories()

    category_id = request.args.get("category_id")
    kw = request.args.get("kw")
    page = request.args.get("page", 1)

    products = doc.get_products(category_id, kw, int(page))

    pages = doc.total_products() / app.config["PAGE_SIZE"]

    return render_template('index.html', categories=categories, products=products, pages=math.ceil(pages))


@app.route("/login")
def login():
    return  render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)
