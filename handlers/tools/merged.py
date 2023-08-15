"""Объединяет служебные записки и объединяет их"""
# +==========================================================+ #
#  GitHub:       https://github.com/AuF22                      #
#  LinkedIn:     https://www.instagram.com/mr_aseev14/         #
#  Instagram:    https://www.linkedin.com/in/altynbek-aseev/   #
#                       © AuF22                                #
# +==========================================================+ #
from openpyxl.worksheet.worksheet import Worksheet


def merged(sheet: Worksheet, cell: int):
    
    full_name = sheet[f"C{cell}"].value
    memo = sheet[f"E{cell}"].value
    solution = sheet[f"G{cell}"].value
    credit_no = sheet[f"C{cell+1}"].value
    
    req = {
        full_name: {
            credit_no: {
                "solution": solution,
                "memo": memo
            }
        }
    }
    print(req)
    return req
    