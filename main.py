import time
print('───────────▄▄▄▄▄▄▄▄▄───────────')
time.sleep(0.1)
print('────────▄█████████████▄────────      ███████╗███████╗███████╗██╗     ██╗   ██╗██╗  ██╗')
time.sleep(0.1)
print('█████──█████████████████──█████      ██╔════╝██╔════╝██╔════╝██║     ██║   ██║╚██╗██╔╝')
time.sleep(0.1)
print('▐████▌─▀███▄───────▄███▀─▐████▌      █████╗  █████╗  █████╗  ██║     ██║   ██║ ╚███╔╝')
time.sleep(0.1)
print('─█████▄──▀███▄───▄███▀──▄█████─      ██╔══╝  ██╔══╝  ██╔══╝  ██║     ██║   ██║ ██╔██╗')
time.sleep(0.1)
print('─▐██▀███▄──▀███▄███▀──▄███▀██▌─      ███████╗██║     ██║     ███████╗╚██████╔╝██╔╝ ██╗')
time.sleep(0.1)
print('──███▄▀███▄──▀███▀──▄███▀▄███──      ╚══════╝╚═╝     ╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝')
time.sleep(0.1)
print('──▐█▄▀█▄▀███─▄─▀─▄─███▀▄█▀▄█▌──')
time.sleep(0.1)
print('───███▄▀█▄██─██▄██─██▄█▀▄███───                     PASSWORD MANAGER')
time.sleep(0.1)
print('────▀███▄▀██─█████─██▀▄███▀────')
time.sleep(0.1)
print('───█▄─▀█████─█████─█████▀─▄█───')
time.sleep(0.1)
print('───███────────███────────███───')
time.sleep(0.1)
print('───███▄────▄█─███─█▄────▄███───')
time.sleep(0.1)
print('───█████─▄███─███─███▄─█████───      𝓒 𝓡 𝓔 𝓐 𝓣 𝓔  𝓝 𝓔 𝓦   𝓐 𝓒 𝓒 𝓞 𝓤 𝓝 𝓣')
time.sleep(0.1)
print('───█████─████─███─████─█████───      ----> ENTER: NEW')
time.sleep(0.1)
print('───█████─████─███─████─█████───')
time.sleep(0.1)
print('───█████─████─███─████─█████───      𝓝 𝓔 𝓦   𝓛 𝓞 𝓖 𝓘 𝓝')
time.sleep(0.1)
print('───█████─████▄▄▄▄▄████─█████───      ----> ENTER: APPEND')
time.sleep(0.1)
print('────▀███─█████████████─███▀────')
time.sleep(0.1)
print('──────▀█─███─▄▄▄▄▄─███─█▀──────      𝓞 𝓟 𝓔 𝓝   𝓥 𝓐 𝓤 𝓛 𝓣')
time.sleep(0.1)
print('─────────▀█▌▐█████▌▐█▀─────────      ----> ENTER: OPEN')
time.sleep(0.1)
print('────────────███████────────────')
print()
print()
from cryptography.fernet import Fernet
import hashlib
s = hashlib.sha3_224()


new_usr=input('enter your choice : ')
if new_usr.lower() == 'append':
    import password

elif new_usr.lower() == 'new':
    mp={}
    emp={}
    import pickle
    file_name=input("Enter your account name: ")
    new_password=input('Enter your master password: ')

    key = Fernet.generate_key()

    encoded_str = new_password.encode()
    obj_sha3_256 = hashlib.sha3_256(encoded_str)
    hash=obj_sha3_256.hexdigest()

    mp['usr_password'] = hash
    mp['key'] = key
    new_file=open(file_name,'wb')
    
    pickle.dump(mp,new_file)
    new_file.close()
    print('New user is successfully created.')
    print('Now run again and add some logins by appending.')

elif new_usr.lower() == 'open':
    import pwd_check