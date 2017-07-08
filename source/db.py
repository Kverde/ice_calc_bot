import psycopg2

sql_log = 'insert into calc_bot.log(user_id, msg, type_msg) values([], ''{}'', 0)'


class Db():

    def __init__(self, setting):
        self.setting = setting

    def insert_log(self, user_id, msg):

        connect = psycopg2.connect(self.setting.database_url)
        cursor = connect.cursor()

        cursor.execute(sql_log.format(user_id, msg))

        connect.commit()
        connect.close()


