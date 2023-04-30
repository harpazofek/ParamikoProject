import time
from secret_password import *
from functions import *

# main():

is_remote = True
ssh_client = ssh_connection(hostname, port, username, password)
trying_time = 0


while is_remote:
    cmd = input(f"enter a command for the remote vm : (or 'q' to quit) ").lower()
    if cmd == 'q':                                  # Check if user wants to quit
        print("Programing Shut Down")
        break
    else:
        print(f"{run_ssh_cmd(ssh_client, cmd)}")
        while True:                                 # Wait for the connection to become active again
            trying_time += 1
            try:
                cmd = "date"                      # Try executing a command on the remote server
                print(f'{run_ssh_cmd(ssh_client, cmd)}SSH connection is active')
                break                               # Exit the loop when the connection is re-active
            except paramiko.SSHException as e:
                print(f"Error executing command: {e}\nSSH connection is not active...")
                time.sleep(5)
                ssh_client.connect(hostname, port, username, password)
                if trying_time >= 10:
                    print(f"\n{trying_time} attempts made. Recursive loop.")
                    is_remote = False
                    break
if ssh_client:        
    ssh_client.close()  
    print(f"Client {hostname} connection close")