from json import load
import random
import string
import os.path
load_key = ''
names = []
def make_key(name):
    global key_dictionary
    names.append(name)
    my_value = list(string.ascii_lowercase)
    my_key = list(string.ascii_lowercase)
    random.shuffle(my_key)
    key_dictionary = dict(zip(my_value, my_key))
    print('A new key called '+ name[0] + ' was created')

def save_key(name):
    if name in names:
        with open(name[0]+'.key', 'w') as f:
            f.write(str(key_dictionary)) 
        print('Enc/Dec'+ name[0] + 'keys saved in ' + name[0] +' file')
    else : print('no such key')


def current_key():
    if load_key != '': 
        with open(load_key,'r') as f:
            key=f.read()
        key=eval(key)
        print('current key is : ' + load_key)
        return load_key
    else : print('not have any key now')


def load(key):
    global load_key
    if not os.path.exists(key[0] + '.key'):
        print('No such key') 
    else:
        load_key=key[0] + '.key'
        print('Key '+ key[0] +' from file ' + key[0] +'.key' +' loaded')
        

def encr(files):
    cipher = ''
    with open(load_key,'r') as f:
        key=f.read()
    key=eval(key)
    with open(files[0],'r') as f:
        plain_text=f.read()
    for letter in plain_text:
        cipher += key[letter]
    with open(files[1], 'w') as f:
        f.write(cipher)
    print('File '+ files[0] +' was encrypted into ' +files[1])
    return(cipher)

def decr(files):
    text = ''
    with open(load_key,'r') as f:
        key=f.read()
    key=eval(key)
    with open(files[0],'r') as f:
        cipher=f.read()
    for letter in cipher:
        text += get_key(letter,key)
    with open(files[1], 'w') as f:
        f.write(text)
    print('File '+ files[0] +' was decrypted into ' +files[1])
    return text


def get_key(val,key):
    for i, value in key.items():
        if val == value:
            return i

def info():
    name=current_key()
    print( 'state : saved in ' + name)