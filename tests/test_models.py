from app.models import User
from app import db

def test_new_user(app):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the username, email, and password fields are defined correctly
    """
    with app.app_context():
        user = User(username='testuser', email='test@test.com', password='hashedpassword')
        db.session.add(user)
        db.session.commit()

        retrieved_user = User.query.filter_by(email='test@test.com').first()
        assert retrieved_user.username == 'testuser'
        assert retrieved_user.email == 'test@test.com'
        assert retrieved_user.password == 'hashedpassword'
        assert retrieved_user.image_file == 'default.jpg'

def test_user_repr(app):
    """
    GIVEN a User model
    WHEN the __repr__ method is called
    THEN check it returns the expected string
    """
    with app.app_context():
        user = User(username='testuser', email='test@test.com', password='hashedpassword')
        db.session.add(user)
        db.session.commit()
        assert repr(user) == "User('testuser', 'test@test.com', 'default.jpg')"
