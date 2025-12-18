from app.models import User
from app import db, bcrypt

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Home Page" in response.data

def test_register_page(client):
    response = client.get('/register')
    assert response.status_code == 200
    assert b"Join Today" in response.data

def test_register_user(client, app):
    response = client.post('/register', data=dict(
        username='testuser',
        email='test@test.com',
        password='password',
        confirm_password='password'
    ), follow_redirects=True)
    
    # After successful registration, it redirects to login page and shows success message
    assert response.status_code == 200
    assert b"Your account has been created!" in response.data
    
    with app.app_context():
        user = User.query.filter_by(email='test@test.com').first()
        assert user is not None
        assert user.username == 'testuser'

def test_login_user(client, app):
    # First create a user
    with app.app_context():
        hashed_password = bcrypt.generate_password_hash('password').decode('utf-8')
        user = User(username='testuser', email='test@test.com', password=hashed_password)
        db.session.add(user)
        db.session.commit()

    # Try to login
    response = client.post('/login', data=dict(
        email='test@test.com',
        password='password'
    ), follow_redirects=True)

    assert response.status_code == 200
    # Logged in users see "Logout" in navbar
    assert b"Logout" in response.data

def test_login_invalid_password(client, app):
    # First create a user
    with app.app_context():
        hashed_password = bcrypt.generate_password_hash('password').decode('utf-8')
        user = User(username='testuser', email='test@test.com', password=hashed_password)
        db.session.add(user)
        db.session.commit()

    response = client.post('/login', data=dict(
        email='test@test.com',
        password='wrongpassword'
    ), follow_redirects=True)

    assert response.status_code == 200
    assert b"Login Unsuccessful" in response.data

def test_logout(client, app):
    # Login first
    with app.app_context():
        hashed_password = bcrypt.generate_password_hash('password').decode('utf-8')
        user = User(username='testuser', email='test@test.com', password=hashed_password)
        db.session.add(user)
        db.session.commit()
    
    client.post('/login', data=dict(
        email='test@test.com',
        password='password'
    ), follow_redirects=True)

    # Logout
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    # Should see Login link again
    assert b"Login" in response.data
    # Use re.search or simply check if Logout is NOT present, but 'Logout' string might be present in other context? 
    # The navbar logic: {% if current_user.is_authenticated %} ... Logout ... {% else %} ... Login ...
    # So if logged out, we shouldn't see "Logout" link.
    # However, be careful if the word Logout appears elsewhere. In this simple app, it's likely fine.
    # Better: check for "Login" link availability which implies logout state.
    assert b"Login" in response.data

def test_account_page_requires_login(client):
    response = client.get('/account', follow_redirects=True)
    # Should be redirected to login page
    assert b"Log In" in response.data
