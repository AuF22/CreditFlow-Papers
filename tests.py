"""Тестим различные вещи"""


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
    similar_list = []
    dissimilar_list = []
    x = len(solution_1) if len(solution_1)>len(solution_2) else len(solution_2)
    for i in range(x):
        try:
            if solution_1[i] in solution_2:
                similar_list.append(solution_1[i])
            else:
                dissimilar_list.append(solution_1[i])
        except IndexError:
            pass
        
        try:
            if solution_2[i] in solution_1:
                similar_list.append(solution_2[i])
            else:
                dissimilar_list.append(solution_2[i])
        except IndexError:
            pass
    print(dissimilar_list)
    print(similar_list)
    # ===============================================================================


sol = [
    'В связи со смертью заемщика:\n1. С процентного счета направить на погашение ссудного счета в сумме 121,90 (Сто двадцать один сом девяносто тыйын);\n2. Списать начисленные проценты с 07.08.2023 г. по 23.08.2023 г. в сумме 245,86 (Двести сорок пять сом восемьдесят шесть тыйын);\n3. Прекратить начисление процентов и штрафных пеней с 24.08.2023 г.\n4. Рекомендуемая классифицикация данного кредита – "потери".\n5. Перенести данный кредит в КП Управляющего Араванским филиалом Абдрашитова И.М. \n6. Ответственным за возврат кредита назначить Каймаматова Абдикасима Маликовича',
    'В связи со смертью заемщика:\n1. Списать начисленные проценты с 07.08.2023 г. по 23.08.2023 г. в сумме 1 119,66 (Одна тысяча сто девятнадцать сом шестьдесят шесть сом);\n2. Прекратить начисление процентов и штрафных пеней с 24.08.2023 г.\n3. Рекомендуемая классифицикация данного кредита – "потери".\n4. Перенести данный кредит в КП Управляющего Араванским филиалом Абдрашитова И.М.\n5. Ответственным за возврат кредита назначить Каймаматова Абдикасима Маликовича']

dog = [
    '№10750799476003 от 24.02.2022 г.',
    '№0560724334007 от 29.03.2023 г.'
        ]


if __name__ == '__main__':
    merged_solitions(
        solution_1=sol[0],
        solution_2=sol[1],
        loan_num_1=dog[0],
        loan_num_2=dog[1]
    )
