"""Тестим различные вещи"""
import json
import os
from fuzzywuzzy import fuzz


date = [
    "от Управляющего Кантским филиалом Чакелеева Дж. о приостановлении начисления процентов и штрафных пеней",
    "от Управляющего Ала-Букинского представительства Тиллабаевой А.С. о приостановлении начисления процентов и штрафных пеней",
    "от Управляющего Ошского филиала Мырзаматова М.Б. о приостановлении начисления процентов и штрафных пеней",
    
    ]




file = f"handlers{os.sep}docs{os.sep}branches.json"
# Открываем сохраненный файл с филиалами
# =========================================
with open(file, "r", encoding="utf-8") as branhes:
    branhes = branhes.read()  # Чтение содержимого файла в строку
    branhes = json.loads(branhes)
    
    for i in date:
        i = i.split(' ')
        for word in i:
            if 'филиал' in word or 'предст' in word:
                temp_branch = i.index(word)
                temp_branch = i[temp_branch-1:temp_branch+1]
                temp_branch = ' '.join(temp_branch)
                
                test_list = map(lambda x: (fuzz.partial_ratio(x, temp_branch), x), branhes) # Не знаю как я сделал, но оно сработало, я в ахуи просто
                temp_list = sorted(list(test_list), key=lambda x: x[0])
                print(f"{temp_branch}, самое близкое значение {branhes[temp_list[-1][1]]}")
                print('*'*66)
    
                    
            elif "офис" in word:
                temp_branch = 'Головной офис'
    
    
    try:
        pass
    except KeyError:
        print("Головной офис")
# =========================================
