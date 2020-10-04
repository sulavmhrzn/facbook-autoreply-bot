from utils.app import SendBot
try:
    from dotenv import load_dotenv
    import os
except ModuleNotFoundError:
    print('Required modules not found.')
    exit()

load_dotenv()

env = input('Load environment variables? (y/n): ').lower()

options = ['y', 'n']

if env in options:
    if env == 'n':
        email = input('Email: ')
        password = input('Password: ')

        if email and password:
            client = SendBot(email, password, max_tries=100)

            # Sets active status
            client.setActiveStatus(markAlive=False)
            client.listen()
        else:
            print('Enter credentials.')
    else:
        client = SendBot(os.getenv('EMAIL'), os.getenv(
            'PASSWORD'), max_tries=100)
        # Sets active status
        client.setActiveStatus(markAlive=False)
        client.listen()
else:
    print('Please type y or n')
