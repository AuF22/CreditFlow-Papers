"""Данная часть кода ответсвенна по обработке протокола Кредитного Комитета"""
# +==========================================================+ #
#  GitHub:       https://github.com/AuF22                      #
#  LinkedIn:     https://www.instagram.com/mr_aseev14/         #
#  Instagram:    https://www.linkedin.com/in/altynbek-aseev/   #
#                       © AuF22                                #
# +==========================================================+ #
import openpyxl
from tkinter.filedialog import askopenfilename
from .check_protocol import LoanCheck
from typing import List
from .docs import creat_docs
from data.db import SQLite
sql = SQLite() # Создаем объект класса


def start_handler() -> List[dict]:
    """
    Запускает обработчик протокола, ничего не принимает, кроме протокола
    который непосредственно пользователемс выбирается. В ответ получаем словарь
    с данными протокола

    Returns:
        List[dict]: Получаем список со всеми данными всловарях (заявки на кредит
        и слежебные записки)
    """
    # Создаем экземпляр класса, а так же собираем общие данные
    # ==============================================================================================================================
    cell = 3                                            # Стартовая ячейка (из-за структуры протокола)
    wb = openpyxl.load_workbook(askopenfilename())      # Создаем экземпляр класса который будем в дальнейшем полностью использовать
    sheet = wb.active                                   # Акстивный лист выбираем
    number_of_com = sheet['B1'].value.split(' ')[-1]    # Номер комитета (из-за структуры протокола)
    date = sheet['I2'].value.strip().split(' ')[1]      # Дата комитете (из-за структуры протокола)
    level = sheet['B1'].value.split(' ')                # 
    level = ' '.join(level).split()                     #
    level = ' '.join(level[1:-2])                       # Получаем уровень комитета Головного офиса
    # ==============================================================================================================================
    
    # Собираем членов кредитного комитета
    # =========================================
    attended = []          # Участники комитета
    # Цикл собирающий перебором всех членов  КК
    while True:
        active_cell = sheet[f'D{cell}'].value
        if active_cell is None: # Останавливаем 
            break
        attended.append(active_cell)
        cell += 1          # Добавляем к ячейке
    # =========================================
    
    data = {
        'number_of_com': number_of_com,
        'date': date,
        'attended': attended,
        'level': level
    }
    print(data['attended'])
    
    cell += 1 # Добавляем к ячейке
    handler = LoanCheck(sheet=sheet, cell=cell) # Инициализация обработчика заявки
    
    request_dict = {}
    service_dict = {}
    # Бесконечный цикл перебирает уже сам протокол 
    # ===============================================================
    while True:
            # В данной точке выбирается обработчик Заявок/Служебок
            selection_point = str(sheet[f'E{cell}'].value).strip()
            
            # Обрабатывается заявки на кредит
            # ========================================================================================================
            if selection_point == 'Цель в «Онлайн Банк»':
                handler.loan_application()  # Метод обработчика
                cell = handler.cell
                request_dict = handler.request_dict
                
            # ========================================================================================================
            
            # Обрабатывает служебные записки 
            # ==========================================
            elif selection_point == 'Служебная записка':
                handler.official_leter()
                service_dict = handler.service_dict
                cell = handler.cell
            # ==========================================
            
            # Это уже конец обработчика, тут создается выписки по шаблонам
            # =====================================================================
            else:
                sql.insert_comit(params=data)
                sql.insert_request(params=request_dict)
                sql.insert_services(params=service_dict)
                creat_docs(data=data, requests=request_dict, services=service_dict)
                break
            # =====================================================================
    # =================================================================


if __name__ == "__main__":
    start_handler()
