"""Initializes keygem

Erick Veil
2013-07-25

Optional argument is file path to database

"""
import os, getpass, subprocess, sys

"""0.1.0"""
def is_db_exists(filepath):
    """checks to see if the db is in the home directory"""

    return os.path.isfile(filepath)

"""0.2.0"""
def create_db(filepath):
    """creates the database
    
    Caution, this will clear out an existing database.
    Obscure caution: is using Tails, you will want to use the backup option to
    save this database in a more persistent location.
    TODO: Perhaps I should have a configuration file that defines the location
    of the database. Or should the user have to provide it as an argument?
    """
    print("creating new database at "+filepath)

    cmd="sqlite "+filepath+" < initdb.sql"
    return subprocess.call(cmd,shell=True) 

"""0.3.0"""
def is_password_set(filepath):
    """placeholder"""
    return True

"""0.4.0"""
def sign_up_user(filepath):
    """placeholder"""
    return True

"""0.5.0"""
def log_in_user(filepath):
    """placeholder"""
    return True

"""0.6.0"""
def is_sqlite_installed():
    """placeholder"""
    return True

"""0.7.0"""
def local_error(msg):
    """deals with errors by wrapping to a more global solution"""
    print(msg)
    return True


"""main"""

if len(sys.argv) > 1:
    filepath=sys.argv[1];
else:
    user=getpass.getuser()
    filepath="/home/"+user+"/.ring.kg"

if not is_db_exists(filepath):
    if is_sqlite_installed():
        create_db(filepath)
    else:
        localError("keygem requires sqlite3 to be installed to work.");

if not is_password_set(filepath):
    user_valid=sign_up_user(filepath)
else:
    user_valid=log_in_user(filepath)

print(user_valid)
