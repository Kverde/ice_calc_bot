from source.ks_math import MathParser

help_text = ''' Поддерживаемые операции +, -, *, /
^ - возведение в степень (2 ^ 10)
! - факториал (5!)
Скобки ( ) для управления порядком вычислений
Константы "e" и "pi"  (pi * 2)
Функции:
sqrt - квадратный корень
abs - модуль числа
sin, cos, tan
'''

about_text = '''Пожалуйста, оцените этого бота https://telegram.me/storebot?start=IceCalcBot

Для связи с разработчиком используйте Telegram @KonstantinShpilko, сайт http://way23.ru
'''

class Domain():
    def on_start(self, bot, update):
        update.message.reply_text(
            'Привет! Отправьте мне математическое выражение и я верну результат. Для получения помощи введите "help" или "?".')

        self.on_help(bot, update)

    def on_help(self, bot, update):
        update.message.reply_text(help_text)

    def on_about(self, bot, update):
        update.message.reply_text(about_text)

    def on_text(self, bot, update):
        text = update.message.text.strip()
        if text == '?' or text == 'help':
            self.on_help(bot, update)
            return 'text_help'

        res = MathParser(text).parse()
        update.message.reply_text(res)
        return 'math'