"""Получает json файлы обрабатывает их и создает по шаблону Выписки"""
# +==========================================================+ #
#  GitHub:       https://github.com/AuF22                      #
#  LinkedIn:     https://www.instagram.com/mr_aseev14/         #
#  Instagram:    https://www.linkedin.com/in/altynbek-aseev/   #
#                       © AuF22                                #
# +==========================================================+ #
from .month import month_name
from docxtpl import DocxTemplate
from .branches import pull_branch
import os
import shutil

# Отрицательные решения Кредитного комитета, нужно для выбора ячейки
solition_t = ["Отказать", "Отправить на доработку"] 


def creat_docs(requests: dict, services: dict, data: dict) -> None:
    """
    Функция создает выписки в формате docx по шаблону

    Args:
        requests (dict): Словарь со всеми собранными заявками
        services (dict): Словарь со всеми собранными служебками
        data (dict): Словарь с общими данными
        
    Returns:
        Ничего не возвращает в папке Documents//Выписки// создается файлы
    """
    # =================================================
    day = data["date"].split('.')[0]                    # День комитета
    month = month_name[int(data["date"].split('.')[1])] # Месяц комитета прописью
    year = data['date'].split('.')[2]                   # Год
    # =================================================
    
    # Создаем папки где будут храниться дкументы
    # ===============================================================
    documents_path = f'{os.path.expanduser("~")}{os.sep}Documents'      # Получаем путь к папке "Документы" пользователя
    new_folder_name = f"Выписки{os.sep}КК ГО {data['number_of_com']}"   # Название создаваемой папки
    new_folder_path = os.path.join(documents_path, new_folder_name)     # Собираем полный путь для новой папки 
    try:
        os.makedirs(new_folder_path)
    except FileExistsError:
        shutil.rmtree(new_folder_path)
        os.makedirs(new_folder_path)
        pass

    # ===============================================================
    if len(requests) != 0: # Если словарь пустой, просто пропускаем
        for i in requests:
            template = DocxTemplate(f"data{os.sep}templates{os.sep}Шаблон_заявка_согл.docx")
            
            temp_dict = {
                "Уровень": data['level'].capitalize(),
                "Номер_комитета": data["number_of_com"],
                "Число": day,
                "Месяц": month,
                "Год": year,
                "ФИО": requests[i]["full_name"],
                "Условие": "на следующих условиях",
                "Решение": requests[i]["answer"],
                "Сумма": requests[i]["sum"],
                "Процент": requests[i]["percent"],
                "Срок": requests[i]["time"],
                "Продукт": requests[i]["product"],
                "Цель": requests[i]['target'],
                "Обеспечение": requests[i]['secured'],
                "Филиал": requests[i]['branch'],
                "Примечание": requests[i]['notice'],
                "Председатель": data['attended'][0]
            }

            if temp_dict["Продукт"] == "Кредитная линия":
                template = DocxTemplate(f"data{os.sep}templates{os.sep}Шаблон_кредитная_линия_согл.docx")
                temp_dict["Метод_погашения"] = requests[i]["type_of_repayment"]
            
            # Изменение шапки решения
            # =====================================================
            if temp_dict["Решение"] == solition_t[0]:
                temp_dict["Условие"] = "и отказана"
            elif temp_dict["Решение"] == solition_t[1]:
                temp_dict["Условие"] = "и отправлена на доработку"
            # =====================================================
            
            template.render(temp_dict)
            template.save(f"{new_folder_path}{os.sep}КК" \
                        + f" {str(temp_dict['Номер_комитета'])}"\
                        + f" {pull_branch(temp_dict['Филиал'], save='request')}"\
                        + f" - {temp_dict['ФИО']}.docx")

    if len(services) !=0: # Если словарь пустой, просто пропускаем
        for i in services:
            if services[i] is None:
                break

            elif 'КП' in services[i]['full_name']:
                pass
            
            template = DocxTemplate(f"data{os.sep}templates{os.sep}Шаблон_служебка.docx")
            temp_dict = {
                "Уровень": data['level'].upper(),
                "Номер_комитета": data["number_of_com"],
                "Число": day,
                "Месяц": month,
                "Год": year,
                "Служебная_записка": services[i]['memo'],
                "Решение": services[i]['solution'],
                "Председатель": data['attended'][0],
                "Секретарь": data["attended"][-1],
                "Члены_КК_ГО": '\n'.join(data["attended"][1::])
            }

            template.render(temp_dict)
            template.save(f"{new_folder_path}{os.sep}ВЫПИСКА ИЗ РКК" \
                        + f" {temp_dict['Номер_комитета']} " \
                        + f"{pull_branch(branch=temp_dict['Служебная_записка'], save='service')} - "
                        + f"{services[i]['full_name']}.docx")
