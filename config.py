import configparser


class ConfigHandler:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")

    @property
    def telegram(self):
        return self.config['Telegram']

    @property
    def mongo(self):
        return self.config['Mongo']

    @property
    def api_id(self):
        return int(self.telegram['api_id'])

    @property
    def api_hash(self):
        return self.telegram['api_hash']

    @property
    def phone(self):
        return self.telegram['phone']

    @property
    def username(self):
        return self.telegram['username']

    @property
    def mongo_uri(self):
        return self.mongo['mongo_uri']
