"""Обрабатываем заявки на кредит"""
# +==========================================================+ #
#  GitHub:       https://github.com/AuF22                      #
#  LinkedIn:     https://www.instagram.com/mr_aseev14/         #
#  Instagram:    https://www.linkedin.com/in/altynbek-aseev/   #
#                       © AuF22                                #
# +==========================================================+ #
from .tools import *
from typing import List, Union
from openpyxl.worksheet.worksheet import Worksheet


# Отрицательные решения Кредитного комитета, нужно для выбора ячейки
solition_t = ["Отказать", "Отправить на доработку"] 


def transition(sheet: Worksheet, cell:int) -> List[Union[int, bool]]:
    """
    Если закончатся заявки отвечает за переход на новую служебные записки или
    для создания выписок
    Args:
        sheet (Worksheet): Лист по которому будет проводиться обработка
        cell (int): Ячейка

    Returns:
        List[Union[int, bool]]: Возвращается список со значением Ячейки и True/False
    """
    # ====================================
    temp = sheet[f"E{cell}"].value
    if temp is None:
        temp_2 = sheet[f"E{cell+1}"].value
        if temp_2 != "Служебная записка":
            return [cell+1, False]
        else:
            return [cell+2, False]
    return [cell, True]
    # ====================================


def notice(sheet: Worksheet, _notice:bool, cell:int, letter: str) -> dict:
    """_summary_

    Args:
        sheet (Worksheet): Лист по которому будет проводиться обработка
        _notice (bool): Для осознаяни есть ли примечание по кредиту или же нету
        cell (int): Ячейка
        letter (str): Буква по которому будет получать данные

    Returns:
        dict: Словарь со всеми готовыми данными по кредиту
    """
    month = sheet[f"{letter}{cell+3}"].value.split(' ')
    sum = num_text_converter(sheet[f"{letter}{cell+1}"].value)
    percent = num_text_converter(int(sheet[f"{letter}{cell+2}"].value*100))
    time = num_text_converter(int(month[0]))
    
    product_and_target = split_target(sheet[f"E{cell}"].value)
    branch = branch_strip(sheet[f"C{cell+3}"].value.strip())
    
    # Словарь со всеми данными
    # ==============================================================================================
    req = {
            'full_name': sheet[f"C{cell}"].value,                               # ФИО клиента
            'branch': branch,                                                   # Отделение
            'target': product_and_target[1],                                    # Цель кредита
            'product': product_and_target[0],                                   # Продукт
            'secured': sheet[f'F{cell}'].value,                                 # Обеспечение
            'answer': sheet[f"G{cell}"].value,                                  # Решение КК
            'sum': f'{sum[0]:_}'.replace('_', ' ')+f' ({sum[1].capitalize()})', # Сумма кредита
            'percent': f'{percent[0]} ({percent[1].capitalize()})',             # Процентная ставка
            'time': f'{time[0]} ({time[1].capitalize()}) {month[1]}',           # Срок кредита
            'notice': None                                                      # Примечания
        }

    if _notice:             # Если же имеется примечания по кредиту, то передаются с другой значения
        req['branch'] = sheet[f"C{cell+4}"].value.strip()                       # Отделение
        req['notice'] = sheet[f'G{cell+4}'].value                               # Примечание
    # ==============================================================================================
    
    return req # Возврат словаря


def solit(sheet: Worksheet, solition: bool, _notice: bool, cell:int) -> dict:
    """_summary_

    Args:
        sheet (Worksheet): Лист по которому будет проводиться обработка
        solition (bool):ЕСли отрицательное решение предпологается, что данные хранятся в ячейке L
        _notice (bool): Для осознаяни есть ли примечание по кредиту или же нету
        cell (int): Ячейка

    Returns:
        dict: Словарь со всеми готовыми данными по кредиту
    """
    if solition:
        # Решение положительное 
        return notice(sheet, _notice, cell, letter='H')
    else:
        # Решение отрицательное
        return notice(sheet, _notice, cell, letter='L')


class LoanApplication():
    """Класс для обработки заявок по кредитам"""
    def __init__(self, sheet: Worksheet, cell: int) -> None:
        """
        Метод инициализациии класс, для сбора первичных переменных передающихся в дальнейшем
        Args:
            sheet (Worksheet): Лист по которому будет проводиться обработка
            cell (int): Ячейка
        """
        self.cell = cell + 1
        self.sheet = sheet
        self.b = None
        self.request_dict = {}

    
    def handler(self):
        """
        Метод запускает всю обработку и посредством него обновляются все парметры класса
        """
        
        sheet = self.sheet  # Лист по которому будет проводиться обработка
        cell = self.cell    # Ячейка
        
        # Получаем решение Положительное/Отрицательное (True/False) 
        # ======================================================
        solution = sheet[f"G{cell}"].value
        solution = True if solution not in solition_t else False
        # ======================================================
        
        
        # Обработка всех данных и запуск всех функций
        # ================================================================
        while True:
            # Заявка с примечанием
            # ============================================================
            if "филиал" in str(sheet[f"C{cell+4}"].value):
                index = sheet[f'B{cell}'].value # Нумерация вопроса КК
                self.request_dict[index] = solit(sheet=sheet, 
                                                 solition=solution, 
                                                 _notice=True, cell=cell)
                transit = transition(sheet=sheet, cell=cell+5)
                
                if transit[1]:
                    cell = transit[0] # Локальное изменение ячейки
                else:
                    self.cell = transit[0] # Глобальное изменение ячейки
                    break
            # =============================================================
            
            
            # Заявка без примечания
            # =============================================================
            else:
                index = sheet[f'B{cell}'].value  # Нумерация вопроса КК
                self.request_dict[index] = solit(sheet=sheet, 
                                                 solition=solution, 
                                                 _notice=False, cell=cell)
                transit = transition(sheet=sheet, cell=cell+4)
                
                if transit[1]:
                    cell = transit[0] # Локальное изменение ячейки
                else:
                    self.cell = transit[0] # Глобальное изменение ячейки
                    break
            # ============================================================
        # ================================================================    
        