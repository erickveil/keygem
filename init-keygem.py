"""Initializes keygem

Checks for first run conditions and maintains initial setup.
Erick Veil
2013-06-24

"""
import json, sys, os, getpass, subprocess

folder_count=0
keyset_flag=False

"""1.0.0"""
def import_autokey_scripts():
    """This gets the scripts used by autokey imported and ready.

        returns False if it fails, preventing the use of autokey with keygem.
        returns True on success.

    """
    used=get_is_fkeys_used()
    if used!=-1 and used:
        return False

    get_is_autokey_running()
    if get_is_autokey_running():
        suspend_autokey()

    inject_into_autokey_config()
    start_autokey()
    touch_key_files()

    return True

"""0.1.0"""
def get_is_fkeys_used():
    """Determines if ctrl-F1/2/3 keys are defined in AutoKey

    returns True if present, false if not, -1 on error
    We don't want to define other keys that might cause conflict.

    """
    global keyset_flag 

    user=get_linux_user_name()
    config_path="/home/"+user+"/.config/autokey/autokey.json"

    try:
        config_file=open(config_path,'r')
    except IOError:
        return -1

    config_obj=json.load(config_file)

    search_folders_for_hotkeys(config_obj)

    config_file.close()

    return keyset_flag

"""0.1.1"""
def get_linux_user_name():
    """Simply returns the linux username, pased on the environment variable."""

    return getpass.getuser()

"""0.1.2"""
def search_folders_for_hotkeys(dic_root):
    """Iterates through the autokey.json object and looks into each "folder"
    member. Looks for "items" keys, and calls a function that looks through the
    keys' members.
    Uses recursion to hit nested folders.
    """
    global folder_count

    for key in dic_root:
        if key=="folders":
            size=len(dic_root[key])
            if size>0:
                for i in range(0,size):
                    search_folders_for_hotkeys(dic_root[key][i])
        elif key=="items":
            search_folder_items(dic_root[key])

"""0.1.2.1"""
def search_folder_items(items_root):
    """the keyset_flag default is false.
    Seaches through a given item and looks at any hotkey components. If found,
    the hotkeys are checked for keys specific to keygem: f1-3, modified by
    ctrl. If found, sets the keyset_flag to true, indicating that we should not
    go inserting code that uses those hotkeys.
    """
    global keyset_flag

    size=len(items_root)
    for i in range(0,size):
        autokey=items_root[i]["hotkey"]["hotKey"]
        mods=items_root[i]["hotkey"]["modifiers"]
        if len(mods)>0 and mods[0]=="<ctrl>":
            if autokey=="<f1>" or autokey=="<f2>" or autokey=="<f3>":
                keyset_flag=True

"""0.2.0"""
def get_is_autokey_running():
    """placeholder"""

    print "hello"
    """result=subprocess.Popen("ps",stdout=subprocess.PIPE)
    for line in result.stdout.readlines():
        print ":"+line
        """

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


