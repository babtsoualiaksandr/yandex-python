

class Robot:
    '''
    Напишите класс Robot, который инициализируется с начальными координатами – 
    положением Робота на плоскости, обе координаты заключены в пределах от 0 до 100.
    Робот может передвигаться на одну клетку вверх (N), вниз (S), вправо (E), влево (W).
    Выйти за границы плоскости Робот не может.

    Метод move() принимает строку – последовательность команд перемещения робота, 
    каждая буква строки соответствует перемещению на единичный интервал в направлении, 
    указанном буквой. Метод возвращает кортеж координат – конечное положение Робота после перемещения.

    Метод path() вызывается без аргументов и возвращает список кортежей координат точек, 
    по которым перемещался Робот при последнем вызове метода move. Если метод не вызывался, 
    возвращает список с одним кортежем – начальным положением Робота.
    '''

    def __init__(self, coordinates):
        self.__x, self.__y = coordinates
        if (self.__x < 0 or self.__x > 99 or self.__y < 0 or self.__y > 99):
            raise Exception("input err")
        self.__history = [(self.__x, self.__y)]

    def move(self, commands):
        for command in commands.upper():
            if command == 'N':
                self.__y += 1
            elif command == 'S':
                self.__y -= 1
            elif command == 'E':
                self.__x += 1
            elif command == 'W':
                self.__x -= 1
            else:
                print('error in command, пропускаем шум')
            if (self.__x > 99):
                self.__x = 99

            if (self.__x < 0):
                self.__x = 0

            if (self.__y > 99):
                self.__y = 99

            if (self.__y < 0):
                self.__y = 0

            self.__history.append((self.__x, self.__y))

        return (self.__x, self.__y)

    def path(self):
        return self.__history


if __name__ == "__main__":
    r = Robot((0, 0))
    print(r.move('NENW'))
    print(*r.path())
