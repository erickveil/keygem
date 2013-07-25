"""Initializes keygem

Erick Veil
2013-07-25

"""

"""0.1.0"""
def is_db_exists():
    """placeholder"""
    return True

"""0.2.0"""
def create_db():
    """placeholder"""

"""0.3.0"""
def is_password_set():
    """placeholder"""
    return True

"""0.4.0"""
def sign_up_user():
    """placeholder"""
    return True

def log_in_user():
    """placeholder"""
    return True


"""main"""
if(!is_db_exists()):
    create_db()

if(!is_password_set()):
    user_valid=sign_up_user()
else:
    user_valid=log_in_user()


