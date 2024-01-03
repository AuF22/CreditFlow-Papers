"""Создаем подключение к Базе данных, для сохранения информации"""
import sqlite3
import os

class SQLite():
    """Класс для работы с БД"""
    def __init__(self) -> None:
        """Инициализация/Подключение к БД"""
        self.connection = sqlite3.connect(f"data{os.sep}db{os.sep}main.db")
        self.general_info = {}
        self.cursor = self.connection.cursor()
        self.id_com = 0
        print('Succefull connection')
        
    def insert_comit(self, params: dict):
        """Записывает данные в БД"""
        query = """{command} FROM committees WHERE number={number} 
        AND date='{date}'""".format(command="{command}",number=params['number_of_com'], date=str(params['date']))
        cursor = self.cursor
        self.general_info = params
        members = ', '.join(params['attended'])
        level = 1 if 'первого' in params['level'] else 2

        check_query = query.format(command='SELECT *')
        
        result = cursor.execute(check_query)
        result = result.fetchall()
        insert_query = f"""INSERT INTO committees
        (number, date, members, level)
        VALUES ({params['number_of_com']},'{str(params['date'])}',
        '{members}', {level})"""

        if len(result) != 0:
            cursor.execute('PRAGMA foreign_keys=on')
            cursor.execute('BEGIN')
            delete_query = query.format(command='DELETE')
            cursor.execute(delete_query)
            cursor.execute('COMMIT')
            print('Удалили')

        cursor.execute('BEGIN')
        cursor.execute(insert_query)
        cursor.execute('COMMIT')
        print('Записали')

        self.id_com = cursor.execute(f"SELECT id_com FROM committees WHERE number={params['number_of_com']} AND date='{str(params['date'])}'").fetchone()[0]
        print(self.id_com)


    def insert_request(self, params:dict):
        """Записыввает Кредитные заявки"""
        cursor = self.cursor
        
        if len(params) != 0:
            for i in params:

                insert_query = f"""INSERT INTO req_credit (
                id_com, full_name, target, product, secured, answer, sum, percent,
                time, notice, branch, comission, type_repay
                ) VALUES (
                {self.id_com}, '{params[i]['full_name']}', '{params[i]['target']}',
                '{params[i]['product']}', '{params[i]['secured']}', '{params[i]['answer']}',
                '{params[i]['sum']}', '{params[i]['percent']}', '{params[i]['time']}',
                '{params[i]['notice']}', '{params[i]['branch']}', '{params[i]['commission']}',
                '{params[i]['type_of_repayment']}'
                )"""

                cursor.execute('BEGIN')
                cursor.execute(insert_query)
                cursor.execute('COMMIT')
    
    def insert_services(self, params:dict):
        """Записывает служебные записки"""
        cursor = self.cursor

        if len(params) != 0:
            
            for i in params:
                if params[i] is None:
                    break

                insert_query = f"""INSERT INTO services (
                id_com, full_name, solution, memo
                ) VALUES (
                {self.id_com}, '{params[i]['full_name']}', '{params[i]['solution']}',
                '{params[i]['memo']}'
                )"""

                cursor.execute('BEGIN')
                cursor.execute(insert_query)
                cursor.execute('COMMIT')
                print('записали')
