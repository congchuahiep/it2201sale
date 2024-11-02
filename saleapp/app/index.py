from flask import render_template, request
import doc
from app import app

@app.route("/")
def index():
    categories = doc.get_categories()

    category_id = request.args.get("category_id")
    kw = request.args.get("kw")

    products = doc.get_products(category_id, kw)

    return render_template('index.html', categories=categories, products=products)

if __name__ == '__main__':
    app.run(debug=True)
