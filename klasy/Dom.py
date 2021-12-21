from klasy.Nieruchomosc import Nieruchomosc


class Dom(Nieruchomosc):
    def __init__(self, miasto: str, ulica: str, powierzchnia: int, cena_za_m2: float, wolnostojacy: bool):
        super().__init__(miasto, ulica, powierzchnia, cena_za_m2)
        self._wolnostojacy = wolnostojacy

    @property
    def wolnostojacy(self) -> bool:
        return self._wolnostojacy

    def __str__(self):
        return super().__str__() + f'Czy dom jest wolnostojacy' \
                                   f' {self._wolnostojacy}'

