from app import app, db
from app.models import Product

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Seed data if empty
        if not Product.query.first():
            products = [
                Product(name='Laptop', price=999.99, description='High performance laptop', image_file='laptop.jpg'),
                Product(name='Smartphone', price=499.99, description='Latest smartphone model', image_file='phone.jpg'),
                Product(name='Headphones', price=199.99, description='Noise cancelling headphones', image_file='headphones.jpg')
            ]
            for p in products:
                db.session.add(p)
            db.session.commit()
            print("Seeded products.")
    app.run(debug=True)
