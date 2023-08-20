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
        
        merged_solition = merged_solitions(
            solution_1=solution_1, solution_2=solution_2,
            loan_num_1=loan_1, loan_num_2=loan_2
            )
        
        memo = f"{memo} заемщика {full_name} по кредитным договорам "+\
                loan_1 + " и " + loan_2
                
        return {'memo': memo, 'solution': merged_solition}
        
    elif loan_type == "single":
        loan_1 = get_loan_num(sheet[f"C{cell+1}"].value)
        memo = f"{memo} заемщика {full_name} по кредитному договору {loan_1}"
        
        solution = sheet[f"G{cell}"].value
        return {'memo': memo, 'solution': solution}
    
    elif loan_type == "none_loan":
        if "КП" in full_name:
            pass
        else:
            return {'memo': memo, 'solution': sheet[f"G{cell}"].value}
