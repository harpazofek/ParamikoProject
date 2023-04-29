# import paramiko

# def ssh_connection(hostname, port, username, password):
#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh.connect(hostname, port, username, password)
#     print("ssh connection")
#     return ssh