import paramiko

target = 'IP'
port = 22
username = open('pass.txt', 'username')
password = 'password'

cmd = "ls"

with paramiko.SSHClient() as client:
    client.load_system_host_keys()
    client.connect(target, port, username, password)
    print(cmd)
    (stdin, stdout, stderr) = client.exec_command(cmd)
    output = stdout.read()
    print(str(output, 'utf8'))