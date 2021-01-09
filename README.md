# Telegram Tracker

Track and save Telegram channel messages into database. This project's core is completely based on [Amir Yousefi](https://github.com/amiryousefi)'s [Telegram Analysis](https://github.com/amiryousefi/telegram-analysis).

## Preparation

- Create Telegram Account
- Get Telegram development credentials in [Telegram API Development Tools](https://my.telegram.org/apps)
- Create Mongo Database

## Configuration

- Create config.ini file (template: [config.temp.ini](./config.temp.ini))
- `api_id` & `api_hash` from [Telegram API Development Tools](https://my.telegram.org/apps)
- `phone` & `username` of Telegram Account
- `mongo_uri` from created Mongo Database

## Channels

- Create a Mongo collection named `channels`
- Find channel ids to tracker. Channel id should be a number with length of 10.
  - You can forward any message from channel to [GetIDs Bot](https://t.me/getidsbot) and get the number from `Origin Chat/id`. -100 prefix should be omitted (`-1001234567890 -> 1234567890`).
  - You can get id from [Telegram Web](https://web.telegram.org) channel url (for some channels). If the url is like https://web.telegram.org/#/im?p=c1234567890_0000000000000000000 then the id is `1234567890` (from c to underscore).
- Add channel ids into `channels` collection (e.g. `{ "id": 1234567890 }`).

## Task

- Run `python main.py` script
- Authenticate telegram from python console (one time)
- A Mongo collection named `histories` will be created.
- Script can be re-run anytime.
- Getting all messages from new channel may take long according to number of messages.
- Getting new messages from existing channel should take average of 1 second.

## To Do

- [ ] Unit Test
