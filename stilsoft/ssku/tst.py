import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.202.10', port=22, username='user', password='stilsoft')
print(f'Connect ')
stdin, stdout, stderr = ssh.exec_command('cd /home/user/rigel/server-app/origin/backend/component-registry/registry/origin; cat package.json')
outer = stdout.read().decode()
for line in outer.split('\n'):
    if 'scud' in line:
        print(line)