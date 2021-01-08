from config_handler import ConfigHandler
from data_handler import DataHandler
from telegram_handler import TelegramHandler
from performance_handler import PerformanceHandler


class TrackingHandler:
    def __init__(self,
                 telegram_handler: 'TelegramHandler',
                 config_handler: 'ConfigHandler',
                 data_handler: 'DataHandler'):
        self.telegram_handler = telegram_handler
        self.config_handler = config_handler
        self.data_handler = data_handler

    async def track(self):
        self.telegram_handler.start()
        await self.telegram_handler.authorize()

        channels = self.data_handler.find_channels()
        for channel in channels:
            channel_id = channel['id']
            str_to_format = "Channel: " + str(channel_id) + " ({:.2f} secs)"
            perf_handler = PerformanceHandler(str_to_format)
            with perf_handler:
                await self.process_channel(channel_id)

    async def process_channel(self, channel_id: int):
        last_id = self.data_handler.get_last_id(channel_id)
        all_messages = []

        my_channel = await self.telegram_handler.get_entity(channel_id)
        self.data_handler.replace_channel(channel_id, my_channel.to_dict())

        while True:
            history = await self.telegram_handler.get_history(my_channel, last_id)
            if not history.messages:
                break
            messages = history.messages
            for message in messages:
                all_messages.append(message)
            last_id = messages[0].id

        self.insert_to_history(all_messages)

    def insert_to_history(self, messages):
        if len(messages) == 0:
            return
        all_messages = []
        for message in messages:
            all_messages.append(message.to_dict())
        self.data_handler.insert_histories(all_messages)
