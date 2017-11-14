from telethon import TelegramClient
from telethon.tl.functions.messages import SendMessageRequest
from telethon.tl.types import UpdateNewChannelMessage
from telethon.tl.types import InputFileLocation
from telethon.tl.functions.upload import GetFileRequest
from telethon.tl.functions.updates import GetStateRequest
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon import TelegramBareClient
import requests

api_id = 118943
api_hash = '63b5861f24c82d96e1dfbd55d3306e9d'
phone_number = '+989213375401'

client = TelegramClient('mySession5', api_id, api_hash, update_workers=2, spawn_read_thread=False)
print(client.connect())
print(client.is_user_authorized())

# peer = client.get_input_entity('alisefidmouy')
# result = client(SendMessageRequest(peer, 'Hello there!'))
# print(result)

print(client(GetStateRequest()))
print(client(ResolveUsernameRequest('alisefidmouy')))
#def get_file_req(client, volume_id, local_id, secret):
#    input_file_location = InputFileLocation(volume_id, local_id, secret)
#    downloaded_file = client(GetFileRequest(input_file_location, 131072, 65536))
#    return downloaded_file
#

input_file_location = InputFileLocation(434327164, 120082, 32068119915613691)
file = open('image.jpg', 'wb')
downloaded_file = client.download_file(input_file_location, file, part_size_kb=None, file_size=None, progress_callback=None)
print(downloaded_file)


# dialogs, entities = client.get_dialogs(10)
# entity = entities[-1]
# print(dialogs)
# print()
# print(entity)


def callback(update):
    zoomg_entity = client.get_entity('computer_ebooks1')
    if isinstance(update, UpdateNewChannelMessage):
        if update.message.to_id.channel_id == zoomg_entity.id:
            print()
            input_file_loc = update.message.media.photo.sizes[-1].location
            print(input_file_loc)

            volume_id = input_file_loc.volume_id
            local_id = input_file_loc.local_id
            secret = input_file_loc.secret

            input_file_location = InputFileLocation(volume_id, local_id, secret)

            file = open('img.jpg', 'wb')
            downloaded_file = client.download_file(input_file_location, file, part_size_kb=None, file_size=None, progress_callback=None)


            # a function call to format json file
            print()


client.add_update_handler(callback)
client.idle()  # ends with Ctrl+C
client.disconnect()
