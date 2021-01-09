from pymongo import MongoClient, DESCENDING

from handler.config_handler import ConfigHandler


class DataHandler:
    def __init__(self, config_handler: 'ConfigHandler'):
        mongo_client = MongoClient(config_handler.mongo_uri)
        self.db = mongo_client.telegram

    def get_history_count(self, channel_id: int):
        return self.db.histories.count_documents({"peer_id.channel_id": channel_id})

    def find_sorted_channel_histories(self, channel_id: int):
        return self.db.histories.find({"peer_id.channel_id": channel_id}).sort("id", DESCENDING)

    def replace_channel(self, channel_id: int, channel):
        return self.db.channels.find_one_and_replace({'id': channel_id}, channel)

    def find_channels(self):
        return self.db.channels.find()

    def insert_histories(self, histories):
        return self.db.histories.insert_many(histories)

    def get_last_id(self, channel_id: int):
        history_count = self.get_history_count(channel_id)
        if history_count == 0:
            return 0
        sorted_channels = self.find_sorted_channel_histories(channel_id)
        last_id = sorted_channels.next()['id']
        return last_id
