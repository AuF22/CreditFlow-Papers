import json, os

class Settings():
    """Класс для работы с настройками"""
    def __init__(self):
        """Инициализация класса
        Обрабатывает файл настроек и создает атрибуты
        """
        # Чтнеие файла настроек (json)
        with open(f"data{os.sep}settings{os.sep}stg.json", "r",encoding="utf-8") as stg:
            settings = json.load(stg)
        

        # ===============================================================
        self.cell = settings["cell"]                                    # Ячейка с которой начинается чтение
        self.main = settings["main"]                                    # Название папки (индекс 0) и файла (индекс 1)
        settings.pop("cell")                                            # Удаляем из словаря ключи
        settings.pop("main")                                            # Удаляем из словаря ключи
        self.stg = settings                                             # Оставшиеся настройки
        # ===============================================================

