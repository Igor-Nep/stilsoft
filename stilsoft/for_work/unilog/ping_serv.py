import subprocess

def ping(host):
    command = subprocess.run(['ping', '-n', '1', host], stdout=subprocess.PIPE)
    return command.returncode == 0


def full_ping(host):
    command = subprocess.run(['ping', host], stdout=subprocess.PIPE)
    return command.returncode == 0


print(ping('192.168.202.9'))
print(full_ping('192.168.202.161'))



