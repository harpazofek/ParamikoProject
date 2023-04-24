class RouterConnection:
    def __init__(self, target, username, password):
        self.target = target
        self.username = username
        self.password = password
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=self.target, username=self.username, password=self.password)
