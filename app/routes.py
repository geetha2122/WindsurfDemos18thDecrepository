from flask import render_template, url_for, flash, redirect, request, session
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User, Product
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)

@app.route("/product/<int:product_id>")
def product(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', title=product.name, product=product)

@app.route("/cart")
def cart():
    if 'cart' not in session:
        session['cart'] = []
    
    # Get product details for items in cart
    cart_items = []
    total_price = 0
    for item_id in session['cart']:
        product = Product.query.get(item_id)
        if product:
            cart_items.append(product)
            total_price += product.price
            
    return render_template('cart.html', title='Shopping Cart', cart_items=cart_items, total_price=total_price)

@app.route("/add_to_cart/<int:product_id>")
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    
    session['cart'].append(product_id)
    session.modified = True
    flash('Product added to cart!', 'success')
    return redirect(url_for('home'))

@app.route("/remove_from_cart/<int:product_id>")
def remove_from_cart(product_id):
    if 'cart' in session:
        try:
            session['cart'].remove(product_id)
            session.modified = True
            flash('Product removed from cart!', 'success')
        except ValueError:
            pass
    return redirect(url_for('cart'))

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
