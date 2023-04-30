import time
from secret_password import *
from functions import *

is_remote = True
ssh_client = ssh_connection(hostname, port, username, password)
trying_time = 0

# cmd = "reboot"
# (stdin, stdout, stderr) = ssh_client.exec_command(cmd)
# output = stdout.read().decode()
# print(f"{output}")

# while not ssh_client and trying_time < 10:
#     time.sleep(10)
#     ssh_client = ssh_connection(hostname, port, username, password)
#     trying_time += 1


while is_remote and ssh_client:
    cmd = input(f"enter a command for the remote vm : (or 'q' to quit) ").lower()
    if cmd == 'q':                                  # Check if user wants to quit
        print("Programing Shut Down")
        break
    else:
        (stdin, stdout, stderr) = ssh_client.exec_command(cmd)
        output = stdout.read().decode()
        print(f"{output}")
        while True:                                 # Wait for the connection to become active again
            trying_time += 1
            try:
                cmd = "date"                      # Try executing a command on the remote server
                stdin, stdout, stderr = ssh_client.exec_command(cmd)
                output = stdout.read().decode()
                print(f"{output}SSH connection is active")
                break                               # Exit the loop when the connection is re-active
            except paramiko.SSHException as e:
                ssh_client.connect(hostname, port, username, password)
                print(f"Error executing command: {e}\nSSH connection is not active... ")
                time.sleep(5)
                if trying_time >= 10:
                    print(f"\n{trying_time} attempts made. Recursive loop.")
                    break
        print("Command Done")
if ssh_client:        
    ssh_client.close()  
    print(f"Client {hostname} connection close")