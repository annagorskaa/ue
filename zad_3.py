class Property:
    def __init__(self, area: str, rooms: int, price: str, address: str) -> None:
        self._area = area
        self._rooms = rooms
        self._price = price
        self._address = address

    @property
    def area(self) -> str:
        return self._area

    @area.setter
    def area(self, value: str) -> None:
        self._area = value

    @property
    def rooms(self) -> int:
        return self._rooms

    @rooms.setter
    def rooms(self, value: int) -> None:
        self._rooms = value

    @property
    def price(self) -> str:
        return self._price

    @price.setter
    def price(self, value: str) -> None:
        self._price = value

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, value) -> None:
        self._address = value

    def __str__(self):
        return f'Właściwości opisujące posiadłość/ nieruchomość' \
               f'powierzchnia - {self.area}, ' \
               f'ilość pokoi: {self.rooms}' \
               f'cena: {self.price}' \
               f'adres - {self.address}'


class House(Property):
    def __init__(self, area: str, rooms: int, price: str, address: str, plot: int) -> None:
        super().__init__(area, rooms, price, address)
        self._plot = plot

    @property
    def plot(self) -> int:
        return self._plot

    @plot.setter
    def plot(self, value: int) -> None:
        self._plot = value

    def __str__(self):
        return f'Dom o właściwościach:' \
               f'powierzchnia - {self.area}, ' \
               f'ilość pokoi: {self.rooms} ' \
               f'cena: {self.price} ' \
               f'adres - {self.address} ' \
               f'o rozmiarze działki {self.plot}'


class Flat(Property):
    def __init__(self, area: str, rooms: int, price: str, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self._floor = floor

    @property
    def floor(self) -> int:
        return self._floor

    @floor.setter
    def floor(self, value: int) -> None:
        self._floor = value

    def __str__(self):
        return f'Mieszkanie o właściwościach: ' \
               f'powierzchnia - {self.area},  ' \
               f'ilość pokoi: {self.rooms} ' \
               f'cena: {self.price} ' \
               f'adres - {self.address} ' \
               f'na piętrze: {self.floor} '


dom = House('tt', 6, '700000 zł', 'Katowice, ul. Chorzowska 51', 62)
mieszkanko = Flat('xx', 2, '375000', 'Katowice, ul. Kwiatowa 23/7', 2)

print(dom)
print(mieszkanko)
