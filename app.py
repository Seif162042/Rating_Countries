from flask import Flask, render_template

app = Flask(__name__)

# Home page route
@app.route('/index.html')
def home():
    return render_template('index.html')

# About page route
@app.route('/about.html')
def about():
    return render_template('about.html')

# Contact page route
@app.route('/contact.html')
def contact():
    return render_template('contact.html')

# Dynamic route: Displaying user profile based on URL parameter
@app.route('/user/<username>')
def user(username):
    return render_template('user.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
