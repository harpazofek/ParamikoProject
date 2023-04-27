import paramiko
import time
from secret_password import *
from functions import *



hostname = '192.168.197.134'
port = 22
# cmd = "df -h"
# is_online = "uptime"

# with paramiko.SSHClient() as client:
#     
#     exit_status = stdout.channel.recv_exit_status()                             # Im use this options to blocking call till the CMD done   

# main()

running = True


while running:
    cmd = "df -h"
# Connect to the remote server
    ssh = ssh_connection(hostname, port, username, password)
    print("ssh")
# Execute the command
    cmd_exec(ssh, cmd)
    print(cmd)
# Wait for to come back up
    waiting_for_online(ssh)
    print(f"{cmd}")
# Close the SSH connection
    ssh.close()
    running = False
print(f"Closed SSH connection to {hostname}")