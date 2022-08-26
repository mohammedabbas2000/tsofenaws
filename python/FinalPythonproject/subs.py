import key
def enc_init():
    commands = {
    'info': enc_info,
    'load':enc_load,
    'newkey':enc_newkey,
    'save':enc_save,
    'enc':encryption,
    'dec':decryption}
    return commands


def main_cli():
    commands = enc_init()
    cli_end = False
    while not cli_end:
        cmd_str = input('subs>')
        cmd = cmd_str.split()
        if cmd and cmd[0] == 'done':
            cli_end = True
        if  cmd:
            commands[cmd[0]](cmd[1:])


def enc_save(name):
    key.save_key(name)

def enc_load(name):
    key.load(name)

def enc_newkey(name):
    key.make_key(name)

def enc_info(*params):
    key.info()

def encryption(files):
    key.encr(files)

def decryption(files):
    key.decr(files)

main_cli()




