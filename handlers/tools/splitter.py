"""Разъединяет продукты"""
# +==========================================================+ #
#  GitHub:       https://github.com/AuF22                      #
#  LinkedIn:     https://www.instagram.com/mr_aseev14/         #
#  Instagram:    https://www.linkedin.com/in/altynbek-aseev/   #
#                       © AuF22                                #
# +==========================================================+ #


def split_target(text: str) -> tuple:
    """_summary_

    Args:
        text (str): Кредитный продукт: Доступный Цель: Торговля

    Returns:
        _type_: (Продукт т.е Доступный, Цель т.е. Торговля)
    """
    
    text = text.split(':')
    product = text[1][:-5].strip()
    target = text[-1].strip()
    
    return (product, target)

def branch_strip(branch: str) -> str:
    branch = branch.split('\n')
    branch = ' '.join(branch)
    return branch