import configparser


class ConfigHandler:
    """
    Read Config values
    """
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")

    @property
    def __telegram(self):
        return self.config['Telegram']

    @property
    def __mongo(self):
        return self.config['Mongo']

    @property
    def api_id(self):
        """
        Get Telegram api id
        """
        return int(self.__telegram['api_id'])

    @property
    def api_hash(self):
        """
        Get Telegram api hash
        """
        return self.__telegram['api_hash']

    @property
    def phone(self):
        """
        Get Telegram phone
        """
        return self.__telegram['phone']

    @property
    def username(self):
        """
        Get Telegram username
        """
        return self.__telegram['username']

    @property
    def mongo_uri(self):
        """
        Get Mongo Uri
        """
        return self.__mongo['mongo_uri']
