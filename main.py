import paramiko
import time
from secret_password import *
from functions import *



cmd = ""
is_online = True


with paramiko.SSHClient() as client:
    client.load_system_host_keys()
    client.connect(hostname, port, username, password)
    
    cmd = input(f'enter a command for the remote vm : (exit when done)')
    # if cmd == "exit" : break
    (stdin, stdout, stderr) = client.exec_command(cmd)
    output = stdout.read()
    print(str(output, 'utf8'))
        # shel1 = client.invoke_shell()
    print(f'checking if the VM is up !')
    while is_online:
    # for i in range(3):
        try:
            print(client.get_host_keys())
            (stdin, stdout, stderr) = client.exec_command("pwd")
            output = stdout.read()
            print(str(output, 'utf8', "VM is UP!"))
            break
        except:
            is_online = True
            print(f'VM is not up yet')
        time.sleep(15)
    client.close()  
    print(f"Client {hostname} connection close")
        