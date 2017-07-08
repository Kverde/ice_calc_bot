from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from lib import botan
from lib.setting import Setting
from source.domain import Domain
from source.db import Db

APP_ID = 'IceCalcBot'

setting = Setting(APP_ID)
domain = Domain()
db = Db(setting)

def botanTrack(message, event_name):
    if setting.botan_token == '':
        return

    uid = message.from_user
    message_dict = message.to_dict()
    botan.track(setting.botan_token, uid, message_dict, event_name)

def insert_log(update):
    db.insert_log(update.message.from_user.id, update.message.text)

def cm_start(bot, update):
    insert_log(update)
    domain.on_start(bot, update)
    botanTrack(update.message, 'start')

def cm_help(bot, update):
    insert_log(update)
    domain.on_help(bot, update)
    botanTrack(update.message, 'help')

def cm_about(bot, update):
    insert_log(update)
    domain.on_about(bot, update)
    botanTrack(update.message, 'about')

def cm_bin(bot, update):
    insert_log(update)
    domain.on_math(bot, update, '/bin', 2)
    botanTrack(update.message, 'bin')

def cm_oct(bot, update):
    insert_log(update)
    domain.on_math(bot, update, '/oct', 8)
    botanTrack(update.message, 'oct')

def cm_hex(bot, update):
    insert_log(update)
    domain.on_math(bot, update, '/hex', 16)
    botanTrack(update.message, 'hex')

def callb_text(bot, update):
    try:
        insert_log(update)
        log_msg = domain.on_text(bot, update, 10)
        botanTrack(update.message, log_msg)
    except Exception as e:
        print(e)
		
updater = Updater(setting.telegram_token)

updater.dispatcher.add_handler(CommandHandler('start', cm_start))
updater.dispatcher.add_handler(CommandHandler('help', cm_help))
updater.dispatcher.add_handler(CommandHandler('about', cm_about))

updater.dispatcher.add_handler(CommandHandler('bin', cm_bin))
updater.dispatcher.add_handler(CommandHandler('hex', cm_hex))
updater.dispatcher.add_handler(CommandHandler('oct', cm_oct))

updater.dispatcher.add_handler(MessageHandler(Filters.text, callb_text))

updater.start_polling()
updater.idle()