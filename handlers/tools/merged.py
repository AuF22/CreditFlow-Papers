"""Объединяет служебные записки и объединяет их"""
# +==========================================================+ #
#  GitHub:       https://github.com/AuF22                      #
#  LinkedIn:     https://www.instagram.com/mr_aseev14/         #
#  Instagram:    https://www.linkedin.com/in/altynbek-aseev/   #
#                       © AuF22                                #
# +==========================================================+ #
from openpyxl.worksheet.worksheet import Worksheet
from typing import Literal
from .service import get_loan_num, merged_solitions


def merged(
    sheet: Worksheet, cell: int, 
    loan_type: Literal["double", "single", "none_loan"]
    ):
    """
    Подготавливает данные для дальнейшей обработки данных

    Args:
        sheet (Worksheet): Лист по которому будет проводиться обработка
        cell (int): Ячейка
        loan_type (Literal[double, single, none_loan]): Параметры для обработки служебок
    """
    
    full_name = sheet[f"C{cell}"].value
    memo = sheet[f"E{cell}"].value
    
    # Двойное решение, т.е. у одного клиента по двум кредитам
    # ============================================================================
    if loan_type == "double":
        print(cell+1)
        loan_1 = get_loan_num(sheet[f"C{cell+1}"].value)    # Первый кредитный договор
        loan_2 = get_loan_num(sheet[f"C{cell+3}"].value)    # Второй кредитный договор
        solution_1 = sheet[f"G{cell}"].value                # Решение по первому кредиту
        solution_2 = sheet[f"G{cell+2}"].value              # Решение по второму кредиту
        merged_solition = merged_solitions(
            solution_1=solution_1, solution_2=solution_2,
            loan_num_1=loan_1, loan_num_2=loan_2
            )
        memo = f"{memo} заемщика {full_name} по кредитным договорам "+\
                loan_1 + " и " + loan_2
        return {'memo': memo, 'solution': merged_solition, 'full_name': full_name}
    # ============================================================================
    
    # Тоже самое, только с одним кредитом
    # =======================================================================
    elif loan_type == "single":
        loan_1 = get_loan_num(sheet[f"C{cell+1}"].value)
        memo = f"{memo} заемщика {full_name} по кредитному договору {loan_1}"
        solution = sheet[f"G{cell}"].value
        return {'memo': memo, 'solution': solution, 'full_name': full_name}
    # =======================================================================
    
    # А тут это, когда нету кредитного довговора
    # ========================================================================================
    elif loan_type == "none_loan":
        if "КП" in full_name:
            # При передаче КП просто переходим дальше
            pass
        else:
            return {'memo': memo, 'solution': sheet[f"G{cell}"].value, 'full_name': full_name}
    # ========================================================================================
