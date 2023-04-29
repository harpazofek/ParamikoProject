import time
from secret_password import *
from functions import *

is_remote = True
ssh = ssh_connection(hostname, port, username, password)
trying_time = 0


while is_remote:
    cmd = input(f"enter a command for the remote vm : (or 'q' to quit) ").lower()
    if cmd == 'q':                                  # Check if user wants to quit
        print("Programing Shut Down")
        is_remote = False
    else:
        (stdin, stdout, stderr) = ssh.exec_command(cmd)
        output = stdout.read().decode()
        print(f"{output}")
        while True:                                 # Wait for the connection to become active again
            trying_time += 1
            try:
                cmd = "whoami"                      # Try executing a command on the remote server
                stdin, stdout, stderr = ssh.exec_command(cmd)
                output = stdout.read().decode()
                print(f"{output}")
                break                               # Exit the loop when the connection is re-active
            except paramiko.SSHException as e:
                print(f"Error executing command: {e}\nWaiting for VM to come back online... ")
                time.sleep(1)
            if trying_time >= 6:
                print(f"\n{trying_time} attempts made. Recursive loop.")
                is_remote = False
        print("Done")
    ssh.close()  
print(f"Client {hostname} connection close")