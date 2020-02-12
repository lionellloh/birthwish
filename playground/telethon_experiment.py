from telethon import TelegramClient, events, sync
import os

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = os.environ["API_ID"]
api_hash = os.environ["API_HASH"]

client = TelegramClient('session_name', api_id, api_hash)
client.start()

print(client.get_me().stringify())

# client.send_message('pakaluppapito', 'Hello! Talking to you from Telethon')
# client.send_file('username', '/home/myself/Pictures/holidays.jpg')

# client.download_profile_photo('me')
# messages = client.get_messages('username')
# messages[0].download_media()

@client.on(events.NewMessage(pattern='(?i)hi|hello'))
async def handler(event):
    await event.respond('Hey! Thanks for your message. I am busy now. Reply later k?')


client.run_until_disconnected()