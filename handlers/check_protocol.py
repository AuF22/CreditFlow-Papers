"""Обрабатывет все заявки, а так же служебные записки"""
# +==========================================================+ #
#  GitHub:       https://github.com/AuF22                      #
#  LinkedIn:     https://www.instagram.com/mr_aseev14/         #
#  Instagram:    https://www.linkedin.com/in/altynbek-aseev/   #
#                       © AuF22                                #
# +==========================================================+ #
from .tools import Worksheet, solition_t, solit, transition, merged


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
            # Заявка с примечанием
            # ============================================================
            if "филиал" in str(sheet[f"C{cell+4}"].value):
                index = sheet[f'B{cell}'].value # Нумерация вопроса КК
                self.request_dict[index] = solit(
                                                sheet=sheet, 
                                                solition=solution, 
                                                _notice=True, 
                                                cell=cell)
                transit = transition(sheet=sheet, cell=cell+5)
                
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
                self.request_dict[index] = solit(
                                                sheet=sheet, 
                                                solition=solution, 
                                                _notice=False, 
                                                cell=cell
                                                )
                transit = transition(sheet=sheet, cell=cell+4)
                
                if transit[1]:
                    cell = transit[0] # Локальное изменение ячейки
                else:
                    self.cell = transit[0] # Глобальное изменение ячейки
                    break
            # ============================================================
        # ================================================================    


    def official_leter(self):
    
        sheet = self.sheet  # Лист по которому будет проводиться обработка
        cell = self.cell + 1    # Ячейка

        while True:
            
            # С кредитным договором
            # =============================
            
            if sheet[f"C{cell+1}"].value is not None:
                index = sheet[f'B{cell}'].value # Нумерация вопроса КК
                
                
                if sheet[f"B{cell+2}"].value is None:
                    self.request_dict[index] = merged(
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
                    self.request_dict[index] = merged(
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
                
                self.request_dict[index] = merged(
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
            