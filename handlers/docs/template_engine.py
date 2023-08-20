"""Получает json файлы обрабатывает их и создает по шаблону Выписки"""
# +==========================================================+ #
#  GitHub:       https://github.com/AuF22                      #
#  LinkedIn:     https://www.instagram.com/mr_aseev14/         #
#  Instagram:    https://www.linkedin.com/in/altynbek-aseev/   #
#                       © AuF22                                #
# +==========================================================+ #
from .month import month_name
from docxtpl import DocxTemplate
import os


def creat_docs(requests: dict, services: dict, data: dict) -> None:

    day = data["date"].split('.')[0]
    month = month_name[int(data["date"].split('.')[1])]
    year = data['date'].split('.')[2]
    # Получаем путь к папке "Документы" пользователя
    documents_path = f'{os.path.expanduser("~")}{os.sep}Documents'

    # Название создаваемой папки
    new_folder_name = f"Выписки{os.sep}КК ГО {data['number_of_com']}"

    # Собираем полный путь для новой папки
    new_folder_path = os.path.join(documents_path, new_folder_name)

    # Создаем папку
    try:
        os.makedirs(new_folder_path)
    except FileExistsError:
        pass

    if len(requests) != 0:
        for i in requests:
            
            template = DocxTemplate(f"data{os.sep}templates{os.sep}Шаблон_заявка_согл.docx")
            temp_dict = {
                "Уровень": data['level'].capitalize(),
                "Номер_комитета": data["number_of_com"],
                "Число": day,
                "Месяц": month,
                "Год": year,
                "ФИО": requests[i]["full_name"],
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

            template.render(temp_dict)
            template.save(f"{new_folder_path}{os.sep}КК ГО {i}.docx")
    if len(services) !=0:
        for i in services:
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
            template.save(f"{new_folder_path}{os.sep}КК ГО {i}.docx")
        