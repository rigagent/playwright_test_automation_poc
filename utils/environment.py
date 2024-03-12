import os
from dotenv import load_dotenv


class Environment:

    def __init__(self):
        load_dotenv()
        self.base_url = os.getenv('URL')
        self.auth_login = os.getenv('AUTH_LOGIN')
        self.auth_password = os.getenv('AUTH_PASSWORD')
