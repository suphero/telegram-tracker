from telethon import TelegramClient, hints
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel, TypeInputPeer

from config import ConfigHandler


class MyTelegramClient:
    def __init__(self, config_handler: 'ConfigHandler'):
        self.username = config_handler.username
        self.api_id = config_handler.api_id
        self.api_hash = config_handler.api_hash
        self.phone = config_handler.phone
        self.limit = 100
        self.telegram_client = TelegramClient(self.username, self.api_id, self.api_hash)

    def connect(self):
        return self.telegram_client.connect()

    def disconnect(self):
        return self.telegram_client.disconnect()

    def start(self):
        return self.telegram_client.start()

    def get_entity(self, entity: 'hints.EntitiesLike'):
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
            limit=self.limit,
            max_id=0,
            min_id=min_id,
            hash=0
        ))


class TelegramHandler:
    def __init__(self, telegram_client: MyTelegramClient):
        self.telegram_client = telegram_client

    async def __aenter__(self):
        await self.telegram_client.connect()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.telegram_client.disconnect()

    def start(self):
        self.telegram_client.start()

    async def get_entity(self, channel_id: int):
        entity = PeerChannel(channel_id)
        return await self.telegram_client.get_entity(entity)

    async def authorize(self):
        authorized = await self.telegram_client.is_user_authorized()
        if not authorized:
            await self.telegram_client.send_code_request()
            try:
                await self.telegram_client.sign_in_code()
            except SessionPasswordNeededError:
                await self.telegram_client.sign_in_password()

    async def get_history(self, peer: 'TypeInputPeer', min_id: int):
        return await self.telegram_client.get_history(peer, min_id)
