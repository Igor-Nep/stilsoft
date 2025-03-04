import paramiko

host = '192.168.202.30'
user = 'user'
pswrd = 'stilsoft'
port = 22

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=pswrd, port=port, look_for_keys=False, allow_agent=False)

ssh = client.invoke_shell()

ssh.send('cd /opt/murom/origin/backend\n')
print(ssh.recv(30000))