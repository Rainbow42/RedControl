class ConfigurationInput:

    def __init__(self,
                 host: str,
                 username: str,
                 password: str,
                 is_one_start: bool = False,
                 port: str = None,
                 secret: str = None):
        self.is_one_start: bool = is_one_start
        self.username = username,
        self.password = password,
        self.host = host

    def validate(self):
        pass

