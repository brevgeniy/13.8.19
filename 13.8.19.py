# Для онлайн-конференции необходимо написать программу, которая будет подсчитывать общую стоимость билетов.
# Программа должна работать следующим образом:
# 1. В начале у пользователя запрашивается количество билетов, которые он хочет приобрести на мероприятие.
# 2. Далее для каждого билета запрашивается возраст посетителя, в соответствии со значением которого выбирается стоимость:
# Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно.
# От 18 до 25 лет — 990 руб.
# От 25 лет — полная стоимость 1390 руб.
# 3. В результате программы выводится сумма к оплате. При этом, если человек регистрирует больше трёх человек на
# конференцию, то дополнительно получает 10% скидку на полную стоимость заказа.
# Для проверки загрузите полученное решение на GitHub и прикрепите ссылку.

n = 0
summa = 0
s = int(input("введите кол-во билетов: ")) # вводится кол-во необходимых билетов
a = [int(input("введите возраст посетителя: ")) for i in range(s)]
while n < s:
    if 18 < a[n] < 25:
        summa = summa + 990
    elif a[n] > 25:
        summa = summa + 1390
    n = n + 1
if s > 3:
    summa = summa * 0.9
print("Итого к оплате: ",int(summa)," рублей")