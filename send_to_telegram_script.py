# Пример скрипта для отправки файла в Telegram
from telegram import Bot
from telegram import InputFile

#def send_to_telegram(pdf_filename, chat_id, bot_token):
 #   bot = Bot(token=bot_token)
  #  bot.send_document(chat_id=chat_id, document=open(pdf_filename, 'rb'))
def send_to_telegram(message_text, chat_id, bot_token):
    bot = Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message_text)
