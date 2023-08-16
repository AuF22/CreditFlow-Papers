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


def merged_solitions (solution_1: str, solution_2: str) -> str:
    pass
    
    
    
    
    
    
    
    
    
    
    