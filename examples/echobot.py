from pytdbot_sync import Client
from pytdbot_sync.types import LogStreamFile, Update
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s][p %(process)d %(threadName)s][%(created)f][%(filename)s:%(lineno)d][%(funcName)s]  %(message)s",
)

client = Client(
    api_id=0,  # Your api_id. You can get it from https://my.telegram.org/
    api_hash="API_HASH",  # Your api_hash. You can get it from https://my.telegram.org/
    database_encryption_key="1234echobot$",  # Your database encryption key
    token="1088394097:AAQX2DnWiw4ihwiJUhIHOGog8gGOI",  # Your bot token. You can get it from https://t.me/botfather
    files_directory="BotDB",  # Path where to store TDLib files
    workers=2,  # Number of workers
    td_verbosity=2,  # TDLib verbosity level
    td_log=LogStreamFile("tdlib.log"),  # Set TDLib log file path
)


@client.on_updateNewMessage()
def print_message(c: Client, message: Update):
    print(message)


@client.on_updateNewMessage()
def echo(c: Client, message: Update):
    if message.content_type == "messageText":
        message.reply_text(message.text, entities=message.entities)

    elif message.content_type == "messageAnimation":
        message.reply_animation(
            message.remote_file_id,
            caption=message.caption,
            caption_entities=message.entities,
        )

    elif message.content_type == "messageAudio":
        message.reply_audio(
            message.remote_file_id,
            caption=message.caption,
            caption_entities=message.entities,
        )

    elif message.content_type == "messageDocument":
        message.reply_document(
            message.remote_file_id,
            caption=message.caption,
            caption_entities=message.entities,
        )

    elif message.content_type == "messagePhoto":
        message.reply_photo(
            message.remote_file_id,
            caption=message.caption,
            caption_entities=message.entities,
        )

    elif message.content_type == "messageSticker":
        message.reply_sticker(message.remote_file_id)

    elif message.content_type == "messageVideo":
        message.reply_video(
            message.remote_file_id,
            caption=message.caption,
            caption_entities=message.entities,
        )

    elif message.content_type == "messageVoiceNote":
        message.reply_voice(
            message.remote_file_id,
            caption=message.caption,
            caption_entities=message.entities,
        )
    else:
        message.reply_text("Oops! i don't know how to handle this message.")


# Run the client
client.run()
