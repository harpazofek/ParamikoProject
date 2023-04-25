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

