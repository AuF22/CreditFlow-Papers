"""Различные помощники для обработки заявок на кредит"""
# +==========================================================+ #
#  GitHub:       https://github.com/AuF22                      #
#  LinkedIn:     https://www.instagram.com/mr_aseev14/         #
#  Instagram:    https://www.linkedin.com/in/altynbek-aseev/   #
#                       © AuF22                                #
# +==========================================================+ #
from .num_text_converter import num_text_converter
from typing import List, Union
from openpyxl.worksheet.worksheet import Worksheet


# Отрицательные решения Кредитного комитета, нужно для выбора ячейки
solition_t = ["Отказать", "Отправить на доработку"] 


def split_target(text: str) -> tuple:
    """
    Разделяет цель и продукт
    Args:
        text (str): Кредитный продукт: Доступный Цель: Торговля

    Returns:
        _type_: (Продукт т.е Доступный, Цель т.е. Торговля)
    """
    
    text = text.split(':')
    product = text[1][:-5].strip()
    target = text[-1].strip()
    
    return (product, target)


def branch_strip(branch: str) -> str:
    branch = branch.split('\n')
    branch = ' '.join(branch)
    return branch


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
    #
    # ====================================
    temp = sheet[f"E{cell}"].value
    if temp is None:
        temp_2 = sheet[f"E{cell+1}"].value
        if temp_2 != "Служебная записка":
            return [cell+1, False]
        else:
            return [cell+1, False]
    return [cell, True]
    # ====================================


def notice(sheet: Worksheet, _notice:bool, cell:int, letter: str) -> dict:
    """
    Собирает параметры по кредиту.

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
    branch = branch_strip(sheet[f"C{cell}"].value.strip())
    
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
    """
    Просто разделение идет (С примечанием/Без примечания)

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
