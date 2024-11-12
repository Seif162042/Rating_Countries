from flask import render_template, request, redirect, url_for, jsonify
from models import Product, db

def init_routes(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/about.html')
    def about():
        return render_template('about.html')

    @app.route('/contact.html')
    def contact():
        return render_template('contact.html')

    @app.route('/index.html')
    def main():
        return render_template('index.html')

    @app.route('/products.html')
    def products():
        products = Product.query.all()
        return render_template('products.html', products=products)

    @app.route('/add', methods=['GET', 'POST'])
    def add_product():
        if request.method == 'POST':
            title = request.form['title']
            description = request.form['description']
            
            new_product = Product(title=title, description=description)
            db.session.add(new_product)
            db.session.commit()
            
            return redirect(url_for('products'))
        
        return render_template('add_product.html')

    @app.route('/update/<int:id>', methods=['GET', 'POST'])
    def update_product(id):
        product = Product.query.get_or_404(id)
        if request.method == 'POST':
            product.title = request.form['title']
            product.description = request.form['description']
            
            db.session.commit()
            return redirect(url_for('products'))
        
        return render_template('update_product.html', product=product)

    @app.route('/delete/<int:id>', methods=['POST'])
    def delete_product(id):
        product = Product.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()
        return redirect(url_for('products'))

    @app.route('/api/products')
    def api_products():
        products = Product.query.all()
        products_data = [{"title": p.title, "description": p.description} for p in products]
        return jsonify(products=products_data)
