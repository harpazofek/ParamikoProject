import paramiko

def ssh_connection(hostname, port, username, password):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.get_host_keys()
    try:
        ssh.connect(hostname, port, username, password)
        print(f"SSH Connected Successfully\nUsername: {username}\nHostname: {hostname}\nPort: {port}\n")
        return ssh
    except Exception as err:
       print(err)
       if err.args[0] == "Authentication failed.":
           print ("conecting to remoet faild, check your cridentials.")
       return None
    
def run_ssh_cmd(ssh_client, cmd):
        (stdin, stdout, stderr) = ssh_client.exec_command(cmd)
        return stdout.read().decode()