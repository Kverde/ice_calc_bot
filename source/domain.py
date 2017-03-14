from source.ks_math import MathParser

help_text = ''' Поддерживаемые операции +, -, *, /
//, div - целочисленное деление
mod - остаток от деления
^, ** - возведение в степень (2 ^ 10 или 2 ** 10)
! - факториал (5!)

+%, -%, *% - операторы для вычисления процентов:
a +% b = a + a * (b / 100)
a -% b = a - a * (b / 100)
a *% b = a * (b / 100)


Скобки ( ) для управления порядком вычислений

Константы "e" и "pi"  (pi * 2)
Функции:
sqrt - квадратный корень
abs - модуль числа
sin, cos, tan



0b6F - числа в двоичной системе
0o343 - числа в восьмеричной системе
0x6F - числа в шестнадцатеричной системе

Доступны команды для вывода результата в нужной системе счисления
/bin - в двоичной
/oct - в восьмеричной
/hex в шестнадцатеричной

Пример: /bin 5 + 6
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

    def on_math(self, bot, update, command, base):
        text = update.message.text[len(command):].strip()
        res = MathParser(text).solve(base)
        update.message.reply_text(res)

    def on_text(self, bot, update, base):
        text = update.message.text.strip()
        if text == '?' or text == 'help':
            self.on_help(bot, update)
            return 'text_help'

        res = MathParser(text).solve(base)
        update.message.reply_text(res)
        return 'math'