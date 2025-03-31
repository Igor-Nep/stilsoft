import os

def env_active():

    if 'VIRTUAL_ENV' in os.environ:
            return True
    return False

if __name__ == "__main__":
    venv_active = env_active()
    if venv_active:
        print('venv активно')
    else:
        print('venv неактивно')

print(os.environ)