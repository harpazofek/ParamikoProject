import paramiko
import time

# Connect to the remote server
def ssh_connection(hostname, port, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port, username, password)
    print("ssh connection")
    return ssh


# Execute the command
def cmd_exec(ssh, cmd):
    stdin, stdout, stderr = ssh.exec_command(cmd)
    output = stdout.read()
    error = stderr.read()
    if error:
        print('Error:', error)
    else:
        print(str(output, 'utf8'))
        print("cmd exec")
    # return True

def is_online(ssh):
    if ssh:
        cmd = "whoami"
        stdin, stdout, stderr = ssh.exec_command(cmd) 
        output = stdout.read()       
        print(str(output, 'utf8'))
        return True
    else:
        print("is offline")
        return False


def waiting_for_online(ssh):
    while not is_online(ssh):
        print("waiting")
        time.sleep(10)
