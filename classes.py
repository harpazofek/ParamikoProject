# import paramiko


# class RouterConnection:
#     def __init__(self, hostname, username, password):
#         self.hostname = hostname
#         self.username = username
#         self.password = password
#         self.client = paramiko.SSHClient()
#         self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         self.client.connect(hostname=self.hostname, username=self.username, password=self.password)
    
#     def execute_command(self, command):
#     stdin, stdout, stderr = self.client.exec_command(command)
#     output = stdout.read().decode('utf-8')
#     return output

#     def close(self):
#         self.client.close()

# import paramiko

# ip = '1.1.1.16'
# username = 'testuser'
# password = 'password'

# remote_conn_pre = paramiko.SSHClient()
# remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)

# command = 'netstat -an | grep 22'
# stdin, stdout, stderr = remote_conn_pre.exec_command(command)
# output = stdout.read().decode()
# print(output)

# remote_conn_pre.close()
