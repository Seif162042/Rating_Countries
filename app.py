from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Routes for original HTML pages
@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')



# Route to display products
@app.route('/products.html')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)

# Route to add a new product
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

# Route to update a product
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_product(id):
    product = Product.query.get_or_404(id)
    if request.method == 'POST':
        product.title = request.form['title']
        product.description = request.form['description']
        
        db.session.commit()
        return redirect(url_for('products'))
    
    return render_template('update_product.html', product=product)

# Route to delete a product
@app.route('/delete/<int:id>', methods=['POST'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('products'))

if __name__ == '__main__':
    app.run(debug=True)
