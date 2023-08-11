"""Прописывает число прописью"""
# +==========================================================+ #
#  GitHub:       https://github.com/AuF22                      #
#  LinkedIn:     https://www.instagram.com/mr_aseev14/         #
#  Instagram:    https://www.linkedin.com/in/altynbek-aseev/   #
#                       © AuF22                                #
# +==========================================================+ #
from typing import Tuple
from .numbers_in_words import ones, teens, tens, hundreds


def num_text_converter(num: int) -> Tuple[int, str]:
    """
    Небольшая функция работающая на рекурсии и возвращающая кортеж 
    (число, пропись)
    На данном этапе работает до миллиардов,
            
    Args:
        num (int): Вводится число которое нужно преобразовать в пропись

    Returns:
        Tuple[int, str]: Возвращается кортеж со входным числом и прописью
    """
    if num <= 0:
        return (num, '')
    if num < 10:
        return (num, ones[num])
    elif num < 20:
        return (num, teens[num])
    elif num < 100:
        if num % 10 == 0:
            return (num, tens[num])
        else:
            text = f"{tens[num//10*10]} {ones[num % 10]}"
            return (num, text)
    elif num < 1_000:
        if num % 100 == 0:
            return (num, hundreds[num])
        else:
            text = f"{hundreds[num//100*100]} "+\
                   f"{num_text_converter(num=num%100)[1]}"
            return (num, text)
    elif num < 1_000_000:
        thousands_descriptor = "тысяч"
        temp_num = num // 1_000
        if temp_num < 5:
            if temp_num == 1:
                text = f"одна тысяча {num_text_converter(num=num%1_000)[1]}"
                text = text.strip()
                print(text)
                return (num, text)
            elif temp_num == 2:
                text = f"две тысячи {num_text_converter(num=num%1_000)[1]}"
                text = text.strip()
                return (num, text)
            else:
                thousands_descriptor = "тысячи"    
        text = f"{num_text_converter(temp_num)[1]} {thousands_descriptor} "+\
               f"{num_text_converter(num=num%1_000)[1]}"
        text = text.strip()
        return (num, text)
    elif num < 1_000_000_000:
        millions_descriptor = "миллионов"
        temp_num = num // 1_000_000
        if temp_num < 5:
            if temp_num == 1:
                millions_descriptor = "миллион"
            else:
                millions_descriptor = "миллиона"  
        text = f"{num_text_converter(temp_num)[1]} {millions_descriptor}"+\
               f"{num_text_converter(num=num%1_000_000)[1]}"
        text = text.strip()
        return (num, text)


if __name__ == "__main__":
    a = num_text_converter(111954312)
    print(a)