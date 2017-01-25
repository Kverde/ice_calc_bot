from source.ks_math import MathParser

help_text = ''' Поддерживаемые операции +, -, *, /
^ - возведение в степень (2 ^ 10)
! - факториал (5!)
Константы "e" и "pi"  (pi * 2)
Функции:
sqrt - квадратный корень
abs - модуль числа
sin, cos, tan
'''

class Domain():
    def on_start(self, bot, update):
        update.message.reply_text(
            'Привет! Отправьте мне математическое выражение и я верну результат. Для получения помощи введите "help" или "?".')

        self.on_help(bot, update)

    def on_help(self, bot, update):
        update.message.reply_text('')
        update.message.reply_text('Для группировки выражений доступны скобки')

    def on_about(self, bot, update):
        update.message.reply_text(r'Для связи с разработчиком используйте Telegram @KonstantinShpilko, сайт http://way23.ru')

    def on_text(self, bot, update):
        text = update.message.text.strip()
        if text == '?' or text == 'help':
            self.on_help(bot, update)
            return 'text_help'

        res = MathParser(text).parse()
        update.message.reply_text(res)
        return 'math'