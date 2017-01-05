import configparser
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from ks_math import MathParser

APP_ID = 'IceCalcBot'

def loadTelegramToken():
    token = os.getenv('TELEGRAM_TOKEN')
    if not token is None:
        return token

    setting_path = os.getenv('ice_setting')
    if setting_path is None:
        raise Exception('System var ice_setting not found')

    settingFileName = os.path.join(setting_path, APP_ID, 'setting.ini')

    if not os.path.exists(settingFileName):
        raise Exception('Setting file {} not found'.format(settingFileName))

    config = configparser.ConfigParser()
    config.read(settingFileName)

    return config['main']['telegram_token']

telegramToken = loadTelegramToken()

def start(bot, update):
    update.message.reply_text('Привет! Отправьте мне математическое выражение и я верну результат. Для получения помощи введите "help" или "?".')
    send_help(bot, update)

def send_help(bot, update):
    update.message.reply_text('Поддерживаемые операции +, -, *, /, ^')
    update.message.reply_text('Для группировки выражений доступны скобки')

def help(bot, update):
    send_help(bot, update)

def text(bot, update):
    try:
        text = update.message.text.strip()
        if text == '?' or text == 'help':
            send_help(bot, update)
            return

        res = MathParser(text).parse()
        update.message.reply_text(res)
    except Exception as e:
        print(e)
		
updater = Updater(loadTelegramToken())

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(MessageHandler(Filters.text, text))

updater.start_polling()
updater.idle()