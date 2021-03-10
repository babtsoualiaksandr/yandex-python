from abc import ABC, abstractmethod
'''
Класс АбстрактныйКот (AbstractCat), который инициализируется без аргументов. Умеет:
– eat – есть. За каждые 10 единиц еды вес увеличивается на 1 единицу, пока не станет 100, 
дальше не растет. Если при одном приеме пищи количество еды не кратно 10, остаток запасается, 
а потом суммируется с новой едой.
– возвращать строковое представление в виде <Имя класса> (вес).

Класс Котенок (Kitten), наследуется от кота с аргументом вес. Умеет мяукать тоненько:
– meow – возвращает строку "meow..."
Еще умеет спать – sleep – возвращает строку Snore, повторенную столько раз, сколько число 
5 помещается в весе.

Класс Кошка (Cat), наследуется от котенка с аргументами вес и кличка. Умеет мяукать громко (meow):
"MEOW..."
и возвращать свое имя (get_name). Также умеет ловить мышей:
– catch_mice – возвращает строку: Got it!
'''


class AbstractCat():

    def __init__(self):
        self.weight = 0
        self.rest = 0

    def eat(self, unit_of_food):
        self.weight += (unit_of_food + self.rest) // 10
        self.rest = (unit_of_food + self.rest) % 10
        if self.weight > 100:
            self.weight = 100

        return type('self')

    def __str__(self):
        return f'{self.__class__.__name__}({self.weight})'


class Kitten(AbstractCat):
    def __init__(self, weight):
        super().__init__()
        self.weight = weight

    def meow(self):
        return "meow..."

    def sleep(self):
        i = self.weight // 5
        str_sleep = 'Snore' * i
        return str_sleep


class Cat(Kitten):
    def __init__(self, weight, name):
        super().__init__(weight)
        self.name = name

    def meow(self):
        return "MEOW..."

    def catch_mice(self):
        return 'Got it!'

    def get_name(self):
        return self.name


if __name__ == "__main__":
    abscat = AbstractCat()
    abscat.eat(125)
    abscat.eat(17)
    print(abscat)
    kit = Kitten(21)
    print(kit.sleep())
    cat = Cat(83, 'Molly')
    print(cat.meow())
    print(cat.get_name())

    kit = Kitten(15)
    kit.eat(24)
    print(kit)
    cat = Cat(41, 'Molly')
    print(cat.catch_mice())
    print(cat)

'''AbstractCat (14)
SnoreSnoreSnoreSnore
MEOW...
Molly

Kitten (17)
Got it!
Cat(41)

AbstractCat(14)
SnoreSnoreSnoreSnore
MEOW...
Molly
Kitten(17)
Got it!
Cat(41)'''
