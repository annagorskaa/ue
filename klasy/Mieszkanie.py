from klasy.Nieruchomosc import Nieruchomosc


class Mieszkanie(Nieruchomosc):
    def __init__(self, miasto: str, ulica: str,
                 powierzchnia: int, cena_za_m2: float, pietro: int):
        super().__init__(miasto, ulica, powierzchnia, cena_za_m2)
        self._pietro = pietro

    @property
    def pietro(self) -> int:
        return self._pietro

    def __str__(self):
        return super().__str__() + f'mieszkanie zlokalizowane' \
                                   f'na pietrze {self._pietro}'
