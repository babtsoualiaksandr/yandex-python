# transport, cars, motorcycles, horse-drawn carts

class Transport():
    transports = []

    def __init__(self, num, speed):
        self.num = num
        self.speed = speed
        Transport.transports.append((int(num), int(speed)))

    @ property
    def num(self):
        return self._num

    @ num.setter
    def num(self, value):
        self._num = value

    @ property
    def speed(self):
        return int(self._speed)

    @ speed.setter
    def speed(self, value):
        self._speed = value


class Horse_drawn(Transport):
    @ classmethod
    def new_horse_drawn_from_str(cls, in_str):
        num, speed = in_str.split(' ')
        return cls(num, speed)

    def __init__(self, num, speed):
        super().__init__(num, speed)


class Car(Transport):
    @ classmethod
    def new_car_from_str(cls, in_str):
        num, speed, petrol = in_str.split(' ')
        return cls(num, speed, petrol)

    def __init__(self, num, speed, petrol):
        if petrol == '98':
            speed = int(speed)
        elif petrol == '95':
            speed = 90 * int(speed) / 100
        elif petrol == '92':
            speed = 80 * int(speed) / 100
        super().__init__(num, speed)


class Motorcycle(Transport):
    @ classmethod
    def new_Motorcycle_from_str(cls, in_str):
        num, speed, petrol = in_str.split(' ')
        return cls(num, speed, petrol)

    def __init__(self, num, speed, petrol):
        if petrol == '98':
            speed = int(speed)
        elif petrol == '95':
            speed = 80 * int(speed) / 100
        elif petrol == '92':
            speed = 40 * int(speed) / 100
        super().__init__(num, speed)


# N, M и t - количеством транспортных средств, длиной трассы и временем гонки соответственно.
if __name__ == "__main__":
    #str_input = input()
    # list_input = str_input.split(' ')
    N = 3 #int(list_input[0])
    M = 100 #int(list_input[1])
    t = 1 # int(list_input[2])
    in_array = ['34 1 80 98', '19 2 90 95', '14 3 30']
    # in_array = ['87 1 100 98', '71 2 50 95']
    
    for tr_input in in_array: #range(N):
        # tr_input = input()
        transport = tr_input.split(' ')
        num = transport[0]
        typet = transport[1]
        speed = int(transport[2])
        if (typet == '1' or typet == '2'):
            petrol = transport[3]

        if (typet == '3'):
            Horse_drawn(num, speed)
        elif (typet == '1'):
            Car(num, speed, petrol)
        elif (typet == '2'):
            Motorcycle(num, speed, petrol)

    print(f'N= {N} M= {M} t= {t}')
    minM = M
    minNum = []
    for item in Transport.transports:
        num, v = item
        print(f'transport = {num} V= {v} l трасса = {M} t={t}  {M - t * v % M}')
        if (minM > M - t * v % M):
            minM = M - t * v % M
            if len(minNum) == 1:
                minNum[0] = num
            else:
                minNum.append(num)
        elif (minM == M - t * v % M):
            minS = M- t * v % M
            minNum.append(num)

    if (len(minNum) == 1):
        print(minNum[0])
    else:
        print(min(minNum))
