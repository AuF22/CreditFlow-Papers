"""Обрабатываем заявки"""
# +==========================================================+ #
#  GitHub:       https://github.com/AuF22                      #
#  LinkedIn:     https://www.instagram.com/mr_aseev14/         #
#  Instagram:    https://www.linkedin.com/in/altynbek-aseev/   #
#                       © AuF22                                #
# +==========================================================+ #
from .tools import *


solition_t = ["Отказать", "Отправить на доработку"]


def transition(sheet, cell:int) -> int:
    """данная функция должна осуществлять переход от заявок к служебкам"""
    temp = sheet[f"E{cell}"].value

    if temp is None:
        temp_2 = sheet[f"E{cell+1}"].value
        if temp_2 != "Служебная записка":
            return [cell+1, False]
        else:
            return [cell+2, False]
    return [cell, True]


def notice(sheet, _notice:bool, cell:int, letter: str) -> dict:
    """Возвращает значания элементов список по в двух формах с примечанием
    или без примечания"""
    
    
    month = sheet[f"{letter}{cell+3}"].value.split(' ')
    sum = num_text_converter(sheet[f"{letter}{cell+1}"].value)
    percent = num_text_converter(int(sheet[f"{letter}{cell+2}"].value*100))
    time = num_text_converter(int(month[0]))
    
    product_and_target = split_target(sheet[f"E{cell}"].value)
    branch = branch_strip(sheet[f"C{cell+3}"].value.strip())
    
    req = {
            'full_name': sheet[f"C{cell}"].value,                               # ФИО клиента
            'branch': branch,                                                   # Отделение
            'target': product_and_target[1],                                    # Цель кредита
            'product': product_and_target[0],                                   # Продукт
            'secured': sheet[f'F{cell}'].value,                                 # Обеспечение
            'answer': sheet[f"G{cell}"].value,                                  # Решение КК
            'sum': f'{sum[0]:_}'.replace('_', ' ')+f' ({sum[1].capitalize()})',  # Сумма кредита
            'percent': f'{percent[0]} ({percent[1].capitalize()})',             # Процентная ставка
            'time': f'{time[0]} ({time[1].capitalize()}) {month[1]}',           # Срок кредита
            'notice': None                                                      # Примечания
        }
    
    if _notice:
        req['branch'] = sheet[f"C{cell+4}"].value.strip()                       # Отделение
        req['notice'] = sheet[f'G{cell+4}'].value                               # Примечание
    
    
    return req


def solit(sheet,solition: bool, _notice: bool, cell:int):
    if solition:
        return notice(sheet, _notice, cell, letter='H')
    else:
        return notice(sheet, _notice, cell, letter='L')


class LoanApplication():
    """Класс для обработки заявок по кредитам"""
    def __init__(self, sheet, cell: int) -> None:
        self.cell = cell + 1
        self.sheet = sheet
        self.b = None
        self.request_dict = {}

    
    def handler(self):
        sheet = self.sheet
        cell = self.cell
        

        solution = sheet[f"G{cell}"].value

        solution = True if solution not in solition_t else False
        
        while True:

            if "филиал" in str(sheet[f"C{cell+4}"].value):
                # Заявка с примечанием
                index = sheet[f'B{cell}'].value
                self.request_dict[index] = solit(sheet=sheet, 
                                                 solition=solution, 
                                                 _notice=True, cell=cell)
                transit = transition(sheet=sheet, cell=cell+5)
                if transit[1]:
                    cell = transit[0]
                    
                else:
                    self.cell = transit[0]
                    break

            else:
                # Заявка без примечания
                index = sheet[f'B{cell}'].value
                self.request_dict[index] = solit(sheet=sheet, 
                                                 solition=solution, 
                                                 _notice=False, cell=cell)
                transit = transition(sheet=sheet, cell=cell+4)
                if transit[1]:
                    cell = transit[0]
                else:
                    self.cell = transit[0]
                    break