class PearsBasket:
    '''
    Итак, у вас есть корзина с грушами и несколько детей. Нужно поделить груши так, 
    чтобы никому из детей не было обидно, то есть поровну. (Теперь понятно, почему в задаче дети?)
    Напишите класс PearsBasket, экземпляр которого при инициализации получает целое число – 
    количество груш в корзине.
    В классе должны быть методы:

    pb // n – деление нацело, возвращает список объектов класса со значениями количества груш
     в каждой корзинке, если есть остаток – он должен находиться в дополнительной последней корзинке.
    pb % n – получение остатка от деления, возвращает число: остаток от деления.
    pb_1 + pb_2 – складываются две корзинки, получается новая корзина;
    pb_1 - n – число вычитается из корзинки, если там есть такое количество груш; 
                                             если нет – вычитается сколько есть, остается 0;
    __str__ – возвращает количество груш в корзине;
    __repr__ – возвращает строку в формате PearsBasket(<количество>).
    '''

    def __init__(self, num_pears):
        self.__num_pears = num_pears

    def __floordiv__(self, n):
        fl_div = self.__num_pears // n
        residue = self.__num_pears % n
        array = []
        for i in range(n):
            array.append(PearsBasket(fl_div))
        if (residue != 0):
            array.append(PearsBasket(residue))
        return array

    def __mod__(self, other):
        return self.__num_pears % other

    def __add__(self, other):
        summa = self.__num_pears + other.__num_pears
        return PearsBasket(summa)

    def __sub__(self, other):
        sub_pb = self.__num_pears - other
        if sub_pb < 0:
            sub_pb = 0
        self.__num_pears = sub_pb

    def __str__(self):
        return (str(self.__num_pears))

    def __repr__(self):
        return f'PearsBasket({self.__num_pears})'


if __name__ == "__main__":
    pb = PearsBasket(17)
    array = pb // 4
    print(array)
    pb_2 = PearsBasket(13)
    pb_3 = pb + pb_2
    print(pb_3)
    print(pb_3 % 7)
    pb - 2
    print([pb])
