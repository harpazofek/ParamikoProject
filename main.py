import paramiko
from pass1 import *
from time import sleep

port = 22
cmd = ""



with paramiko.SSHClient() as client:
    client.load_system_host_keys()
    client.connect(target, port, username, password)
    while True:
        cmd = input(f'enter a command for the remote vm : (exit when done)')
        if cmd == "exit" : break
        (stdin, stdout, stderr) = client.exec_command(cmd)
        output = stdout.read()
        print(str(output, 'utf8'))
        shel1 = client.invoke_shell()
    for i in range(3):
        print(f'checking if the VM is up !')
        try:
            print(client.get_host_keys())
            (stdin, stdout, stderr) = client.exec_command("pwd")
            output = stdout.read()
            print(str(output, 'utf8'))
        except:
            print(f'VM is not up yet')
        sleep(10)    
    client.close()  
        