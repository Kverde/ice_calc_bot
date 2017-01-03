import configparser

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from ks_math import MathParser

config = configparser.ConfigParser()
config.read('settings.ini')


def start(bot, update):
    print('start')
    update.message.reply_text('Hello! Send me mathematical expression!')

def hello(bot, update):
    print('hello')
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def text(bot, update):
    print('text ' + update.message.text)
    try:
        res = MathParser(update.message.text).parse()
        update.message.reply_text(res)
    except Exception as e:
        print(e)
		
updater = Updater(config['main']['telegram_token'])

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(MessageHandler(Filters.text, text))

updater.start_polling()
updater.idle()