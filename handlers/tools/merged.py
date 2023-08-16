"""Объединяет служебные записки и объединяет их"""
# +==========================================================+ #
#  GitHub:       https://github.com/AuF22                      #
#  LinkedIn:     https://www.instagram.com/mr_aseev14/         #
#  Instagram:    https://www.linkedin.com/in/altynbek-aseev/   #
#                       © AuF22                                #
# +==========================================================+ #
from openpyxl.worksheet.worksheet import Worksheet
from typing import Literal
from .service import get_loan_num


def merged(
    sheet: Worksheet, cell: int, 
    loan_type: Literal["double", "single", "none_loan"]
    ):
    """_summary_

    Args:
        sheet (Worksheet): _description_
        cell (int): _description_
        loan_type (Literal[&quot;double&quot;, &quot;single&quot;, &quot;none_loan&quot;]): _description_
    """
    
    full_name = sheet[f"C{cell}"].value
    memo = sheet[f"E{cell}"].value
    

    if loan_type == "double":
        loan_1 = get_loan_num(sheet[f"C{cell+1}"].value)
        loan_2 = get_loan_num(sheet[f"C{cell+3}"].value)
        solution_1 = sheet[f"G{cell}"].value
        solution_2 = sheet[f"G{cell+2}"].value
        
        memo = f"{memo} заемщика {full_name} по кредитным договорам "+\
                loan_1 + " " + loan_2
                
        print(f"Двойная\n{memo=}")
        
        
    elif loan_type == "single":
        loan_1 = get_loan_num(sheet[f"C{cell+1}"].value)
        memo = f"{memo} заемщика {full_name} по кредитному договору {loan_1}"
        
        solution = sheet[f"G{cell}"].value
        print(f"Одиночная\n {memo=}")
    
    elif loan_type == "none_loan":
        if "КП" in full_name:
            print("Отработан КП")
        else:
            print(memo)
