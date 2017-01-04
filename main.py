import configparser
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from ks_math import MathParser

APP_ID = 'IceCalcBot'

setting_path = os.getenv('ice_setting')
if setting_path is None:
    raise Exception('System var ice_setting not found')

settingFileName = os.path.join(setting_path, APP_ID, 'setting.ini')

if not os.path.exists(settingFileName):
    raise Exception('Setting file {} not found'.format(settingFileName))

config = configparser.ConfigParser()
config.read(settingFileName)


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