from telethon.errors import SessionPasswordNeededError
from telethon.tl.types import PeerChannel, TypeInputPeer

from telegram_client import MyTelegramClient


class TelegramHandler:
    def __init__(self, telegram_client: MyTelegramClient):
        self.telegram_client = telegram_client

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
