"""Initializes keygem

Checks for first run conditions and maintains initial setup.
Erick Veil
2013-06-24

"""
import json, sys, os

"""1.0.0"""
def import_autokey_scripts():
    """This gets the scripts used by autokey imported and ready.

        returns False if it fails, preventing the use of autokey with keygem.
        returns True on success.

    """
    if get_is_fkeys_used():
        return False

    if get_is_autokey_running():
        suspend_autokey()

    inject_into_autokey_config()
    start_autokey()
    touch_key_files()

    return True

"""0.1.0"""
def get_is_fkeys_used():
    """Determines if ctrl-F1/2/3 keys are defined in AutoKey

    returns True if present, false if not.
    We don't want to define other keys that might cause conflict.

    """
    user=get_linux_user_name()
    config_path="/home/"+user+"/.config/autokey/autokey.json"
    
    config_file=open(config_path,'r')

    config_obj=json.load(config_file)
    print config_obj

    config_file.close()


    return True

"""0.1.1"""
def get_linux_user_name():
    """placeholder"""

    return "amnesia"

"""0.2.0"""
def get_is_autokey_running():
    """placeholder"""

    return True

"""0.3.0"""
def suspend_autokey():
    """placeholder"""

"""0.4.0"""
def inject_into_autokey_config():
    """placeholder"""


"""0.5.0"""
def start_autokey():
    """placeholder"""


"""0.6.0"""
def touch_key_files():
    """placeholder"""

"""unit test"""
test=import_autokey_scripts()
print test


