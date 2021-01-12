from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import TypeInputPeer
from telethon.hints import EntitiesLike

from handler.config_handler import ConfigHandler


class MyTelegramClient:
    """
    Telegram Client
    """
    def __init__(self, config_handler: 'ConfigHandler'):
        self.phone = config_handler.phone
        self.telegram_client = TelegramClient(config_handler.username, config_handler.api_id, config_handler.api_hash)

    async def __aenter__(self):
        await self.telegram_client.connect()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.telegram_client.disconnect()

    def start(self):
        """
        Start client
        """
        return self.telegram_client.start()

    def get_entity(self, entity: 'EntitiesLike'):
        return self.telegram_client.get_entity(entity)

    def is_user_authorized(self):
        return self.telegram_client.is_user_authorized()

    def send_code_request(self):
        return self.telegram_client.send_code_request(self.phone)

    def sign_in_code(self):
        return self.telegram_client.sign_in(self.phone, input('Enter the code: '))

    def sign_in_password(self):
        return self.telegram_client.sign_in(password=input('Password: '))

    def get_history(self, peer: 'TypeInputPeer', min_id: int):
        return self.telegram_client(GetHistoryRequest(
            peer=peer,
            offset_id=0,
            offset_date=None,
            add_offset=0,
            limit=100,
            max_id=0,
            min_id=min_id,
            hash=0
        ))
