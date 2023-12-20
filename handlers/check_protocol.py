"""Обрабатывет все заявки, а так же служебные записки"""
# +==========================================================+ #
#  GitHub:       https://github.com/AuF22                      #
#  LinkedIn:     https://www.instagram.com/mr_aseev14/         #
#  Instagram:    https://www.linkedin.com/in/altynbek-aseev/   #
#                       © AuF22                                #
# +==========================================================+ #
from .tools import Worksheet, solition_t, notice, transition, merged, split_target

class LoanCheck():
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
        self.request_dict = {}
        self.service_dict = {}

    
    def loan_application(self):
        """
        Метод запускает всю обработку и посредством него обновляются все парметры класса
        """
        
        sheet = self.sheet  # Лист по которому будет проводиться обработка
        cell = self.cell    # Ячейка
        
        # Обработка всех данных и запуск всех функций
        # ================================================================
        while True:
            # Получаем решение Положительное/Отрицательное (True/False) 
            # ======================================================
            solution = sheet[f"G{cell}"].value
            solution = True if solution not in solition_t else False
            # ======================================================
            
            # Проверяем продукт "Кредитная линия" (У нее другая структура)
            # ============================================================
            credit_line = True if 'Кредитная линия' == str(split_target(sheet[f"E{cell}"].value)[0]) else False
            allowance = 6 if credit_line else 4
            # ============================================================

            division_point = str(sheet[f"C{cell+allowance}"].value)
            # Заявка с примечанием
            # ============================================================
            if "филиал" in division_point or "представит" in division_point:
                index = sheet[f'B{cell}'].value # Нумерация вопроса КК
                self.request_dict[index] = notice(
                                                sheet=sheet, 
                                                solition=solution, 
                                                _notice=True, 
                                                cell=cell,
                                                allowance=allowance,
                                                credit_line=credit_line
                                                )
                transit = transition(sheet=sheet, cell=cell+allowance+1)
                
                if transit[1]:
                    cell = transit[0] # Локальное изменение ячейки
                else:
                    self.cell = transit[0]# Глобальное изменение ячейки
                    break
            # =============================================================
            
            # Заявка без примечания
            # =============================================================
            else:
                index = sheet[f'B{cell}'].value  # Нумерация вопроса КК
                self.request_dict[index] = notice(
                                                sheet=sheet, 
                                                solition=solution, 
                                                _notice=False, 
                                                cell=cell,
                                                allowance=allowance,
                                                credit_line=credit_line
                                                )
                transit = transition(sheet=sheet, cell=cell+allowance)
                
                if transit[1]:
                    cell = transit[0] # Локальное изменение ячейки
                else:
                    self.cell = transit[0] # Глобальное изменение ячейки
                    break
            # ============================================================
        # ================================================================    


    def official_leter(self):
        """
        Метод запускает всю обработку и посредством него обновляются все парметры класса
        """
            
        sheet = self.sheet  # Лист по которому будет проводиться обработка
        
        # Проверка,для установки первичной точки
        # =============================
        if len(self.request_dict) == 0:
            cell = self.cell
        else:     
            cell = self.cell + 1
        # =============================
        
        while True:
            
            # С кредитным договором
            # =============================
            if sheet[f"C{cell+1}"].value is not None:
                
                if sheet[f"B{cell+2}"].value is None:
                    index = sheet[f'B{cell}'].value # Нумерация вопроса КК
                    self.service_dict[index] = merged(
                                                    sheet=sheet, 
                                                    cell=cell, 
                                                    loan_type="double"
                                                    )
                    
                    transit = transition(sheet=sheet, cell=cell+4)
                    
                    if transit[1]:
                        cell = transit[0] # Локальное изменение ячейки
                    else:
                        self.cell = transit[0] # Глобальное изменение ячейки
                        break
                    
                else:
                    index = sheet[f'B{cell}'].value # Нумерация вопроса КК
                    self.service_dict[index] = merged(
                                                    sheet=sheet, 
                                                    cell=cell, 
                                                    loan_type="single"
                                                    )
                    
                    transit = transition(sheet=sheet, cell=cell+2)
                    if transit[1]:
                        cell = transit[0] # Локальное изменение ячейки
                    else:
                        self.cell = transit[0] # Глобальное изменение ячейки
                        break                    
            # =============================

            # Без кредитного договора передача КП, разрешение на выдачу и т.п.
            # =========================
            else:
                index = sheet[f'B{cell}'].value # Нумерация вопроса КК
                self.service_dict[index] = merged(
                                sheet=sheet, 
                                cell=cell, 
                                loan_type="none_loan"
                                )
                
                transit = transition(sheet=sheet, cell=cell+2)
                if transit[1]:
                    cell = transit[0] # Локальное изменение ячейки
                else:
                    self.cell = transit[0] # Глобальное изменение ячейки
                    break      
            # =========================
