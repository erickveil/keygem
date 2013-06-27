"""Initializes keygem

Checks for first run conditions and maintains initial setup.
Erick Veil
2013-06-24

required argument: the name of the template file to be imported into autokey.
The file must be a json file in the format exported by autokey.

"""
import json, sys, os, getpass, subprocess, signal

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
        if not get_is_autokey_running():
            start_autokey()
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

    returns True if present, false if not, -1 on error
    We don't want to define other keys that might cause conflict.

    """
    global keyset_flag 

    config_obj=load_autokey_config()
    search_folders_for_hotkeys(config_obj)

    return keyset_flag

"""0.1.1"""
def get_linux_user_name():
    """Simply returns the linux username, pased on the environment variable."""

    return getpass.getuser()

"""0.1.2"""
def search_folders_for_hotkeys(dic_root):
    """Determines if the hotkeys have been defined.
    
    Iterates through the autokey.json object and looks into each "folder"
    member. Looks for "items" keys, and calls a function that looks through the
    keys' members.
    Uses recursion to hit nested folders.
    """

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
    """Looks for defined hotkey inside a folder list
    
    The keyset_flag default is false.
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

"""0.1.3"""
def load_autokey_config():
    """returns the loaded json object"""
    user=get_linux_user_name()
    config_path="/home/"+user+"/.config/autokey/autokey.json"

    return load_json(config_path)

"""0.2.0"""
def get_is_autokey_running():
    """Uses the shell to check if a process is running.

    This appears to work better than any sorting through the contents of /proc
    trying to determine if one of the files there is what I'm looking for.
    """

    is_running=subprocess.call("ps -A | grep autokey > /dev/null",shell=True)
    if(is_running==0):
        return True
    else:
        return False

"""0.3.0"""
def suspend_autokey():
    """Kills the outokey process.
    
    You should first check to make sure it's running.
    Returns true if succeeds, false if it fails.
    """

    proc=subprocess.Popen(["pgrep","autokey"],stdout=subprocess.PIPE)
    for pid in proc.stdout:
        os.kill(int(pid),signal.SIGTERM)

    return get_is_autokey_running()

"""0.4.0"""
def inject_into_autokey_config():
    """Performs an import of the argument into autokey"""

    config_obj=load_autokey_config()
    template=load_template()

    user=get_linux_user_name()
    config_path="/home/"+user+"/.config/autokey/autokey.json"
    try:
        config_file=open(config_path,'w')
    except IOError:
        return -1

    for key in config_obj:
        if key=="folders":
            config_obj[key]=config_obj[key]+template
            break

    json.dump(config_obj,config_file)

    config_file.close()


"""0.4.1"""
def load_template():
    """loads the template into paths
    gets the template name from the first argument
    """
    path=os.path.dirname(os.path.abspath(__file__))
    path+=("/"+sys.argv[1])

    return load_json(path)

"""0.4.1.1"""
def load_json(path):
    """a more generic way to load paths sinsce I do this multiple times"""

    try:
        config_file=open(path,'r')
    except IOError:
        return -1

    config_obj=json.load(config_file)
    config_file.close()

    return config_obj

"""0.5.0"""
def start_autokey():
    """launches autokey without any command line output"""

    os.system("autokey > /dev/null 2>&1 &")

"""0.6.0"""
def touch_key_files():
    """placeholder"""

    path=os.path.dirname(os.path.abspath(__file__))
    path+=("/")
    file_list=["cf1","cf2","cf3"]

    for i in range(3):
        filename=path+file_list[i]
        if not os.path.exists(filename):
            open(filename, 'w').close()

"""main"""
ex_val=import_autokey_scripts()

if(ex_val==True):
    sys.exit(0)
elif(ex_val==False):
    sys.exit(1)
else:
    sys.exit(2)



