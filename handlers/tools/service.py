"""Различные помощники для обработки служебных записок"""
# +==========================================================+ #
#  GitHub:       https://github.com/AuF22                      #
#  LinkedIn:     https://www.instagram.com/mr_aseev14/         #
#  Instagram:    https://www.linkedin.com/in/altynbek-aseev/   #
#                       © AuF22                                #
# +==========================================================+ #


def get_loan_num(letter: str) -> str:
    """
    Получает строку с кредитным договором, немного переделывает 
    и достает только номер договора

    Args:
        letter (str): кредитный договор №0590849008010 от 26.09.2023 г.

    Returns:
        str:  №0590849008010 от  26.09.2023 г.
    """
    # ===========================================================================
    letter = letter.split(' ')          # Разделяем по пробелам и получаем список
    letter = ' '.join(letter).split()   # Удаляет пустые значения в списке
    letter = ' '.join(letter[-4:])      # Объединяет список
    # ===========================================================================
    
    return letter


def merged_solitions (
    solution_1: str, solution_2: str,
    loan_num_1: str, loan_num_2: str
    ) -> str:
    """
    Объединяет два решения из протокола, сохранив всю структуру и 
    отформатировав текст.
    Args:
        solution_1 (str): Решение комитета
        solution_2 (str): Решение комитета
        loan_num_1 (str): Номер договора
        loan_num_2 (str): Номер договора

    Returns:
        str: Готовый текст который можно просто вставить
    """
    
    # Создаем список для перебора
    # =================================
    solution_1 = solution_1.split('\n')
    solution_2 = solution_2.split('\n')
    # =================================
    
    i = 0 # Номер ирерации
    
    merged_list = [] # Список который будет наполнять
    
    # Вся магия програмиования со строками
    # ===============================================================================
    for letter_1 in solution_1:
        letter_2 = solution_2[i]
        i += 1

        if letter_1 == letter_2:
            # Текст идеинтичный вставляем только один
            merged_list.append(letter_1)
        else:
            # Текст разный придется форматировать
            ii = 0 # Номер итерации для второго перебора
            # Второй перебор для форматирования текста
            for l in letter_1:
                if l == letter_2[ii]:
                    ii += 1
                else:
                    break
            letter_1 = f"{letter_1[0:ii]}\nпо кредитному договору {loan_num_1}: " +\
                        f"{letter_1[ii:]}\nпо кредитному договору {loan_num_2}: " +\
                        f"{letter_2[ii:]}"
            merged_list.append(letter_1)
    # ===============================================================================
    
    
    merged_list = '\n'.join(merged_list)
    
    # Не выглядит красиво, но свою работу полностью выполняет
    # =====================================================================
    merged_list = merged_list.replace('данного кредита', 'данных кредитов')
    merged_list = merged_list.replace('данный кредит', 'данные кредиты')
    merged_list = merged_list.replace('кредита', 'кредитов')
    # =====================================================================
    
    return merged_list # Возврат полностью оформленного текста

    
    
    
    
    
    
    