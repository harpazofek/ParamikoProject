import paramiko
 
ip = '1.1.1.16'
username = 'testuser'
password = 'password'

remote_conn_pre = paramiko.SSHClient()
remote_conn_pre
# paramiko.SSHClient object at 0x15f47d0>

remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
print("netstat -an | grep 22")
