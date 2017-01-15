from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from lib import botan
from lib.setting import Setting
from source.domain import Domain

APP_ID = 'IceCalcBot'

setting = Setting(APP_ID)
domain = Domain()

def botanTrack(message, event_name):
    if setting.botan_token == '':
        return

    uid = message.from_user
    message_dict = message.to_dict()
    botan.track(setting.botan_token, uid, message_dict, event_name)


def cm_start(bot, update):
    domain.on_start(bot, update)
    botanTrack(update.message, 'start')

def cm_help(bot, update):
    domain.on_help(bot, update)
    botanTrack(update.message, 'help')

def callb_text(bot, update):
    try:
        log_msg = domain.on_text(bot, update)
        botanTrack(update.message, log_msg)
    except Exception as e:
        print(e)
		
updater = Updater(setting.telegram_token)

updater.dispatcher.add_handler(CommandHandler('start', cm_start))
updater.dispatcher.add_handler(CommandHandler('help', cm_help))
updater.dispatcher.add_handler(MessageHandler(Filters.text, callb_text))

updater.start_polling()
updater.idle()