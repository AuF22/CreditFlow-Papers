"""Данная часть кода ответсвенна по обработке протокола Кредитного Комитета"""
# +==========================================================+ #
#  GitHub:       https://github.com/AuF22                      #
#  LinkedIn:     https://www.instagram.com/mr_aseev14/         #
#  Instagram:    https://www.linkedin.com/in/altynbek-aseev/   #
#                       © AuF22                                #
# +==========================================================+ #
import openpyxl
from tkinter.filedialog import askopenfilename
from .request import LoanApplication


def start_handler():
    """ """
    cell = 3
    wb = openpyxl.load_workbook(askopenfilename())
    sheet = wb.active
    # Получаем номер комитете
    number_of_com = sheet['B1'].value.split(' ')[-1]
    # получаем дату КК
    date = sheet['I2'].value.strip().split(' ')[1]
    
    # надо получить членов КК
    # =========================================
    attended = [] # Участники комитета
    while True:
        active_cell = sheet[f'D{cell}'].value
        if active_cell is None:
            break
        attended.append(active_cell)
        cell += 1
    # ==========================================
    
    
    cell += 1
    
    
    while True:
        # В данной точке выбирается обработчик Заявок/Служебок
            selection_point = str(sheet[f'E{cell}'].value).strip()
            
            if selection_point == 'Цель в «Онлайн Банк»':
                # Обрабатываются заявки
                a = LoanApplication(sheet=sheet, cell=cell)
                a.handler()
                cell = a.cell
                print(cell)
                print(a.request_dict)
        
            elif selection_point == 'Служебная записка':
                # Обрабатываются служебки
                print("Сработал")
                cell += 1
            
            else:
                # Заканчивает работу обработчика
                print("все")
                
                break


if __name__ == "__main__":
    start_handler()
