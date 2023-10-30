# Пример скрипта для отправки файла в Telegram
import telegram
from telegram import Bot
from telegram import InputFile
import asyncio

#def send_to_telegram(pdf_filename, chat_id, bot_token):
# bot = Bot(token=bot_token)
 # await bot.send_document(chat_id=chat_id, document=open(pdf_filename, 'rb'))
 # asyncio.run(send_to_telegram("Pipeline done!!!", "-4034846321", "6736380758:AAEk-JiTfhLRHJQH99d2AJf1pjeJf0Vv9K4"))
#def send_to_telegram(message_text, chat_id, bot_token):
#    bot = Bot(token=bot_token)
#    bot.send_message(chat_id=chat_id, text=message_text)


#import asyncio
#from telegram import Bot

async def send_to_telegram(message_text, chat_id, bot_token):
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message_text)
asyncio.run(send_to_telegram("Pipeline done!!!", "-4034846321", "6736380758:AAEk-JiTfhLRHJQH99d2AJf1pjeJf0Vv9K4"))