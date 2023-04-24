def execute_command(self, command):
    stdin, stdout, stderr = self.client.exec_command(command)
    output = stdout.read().decode('utf-8')
    return output


def close(self):
    self.client.close()
