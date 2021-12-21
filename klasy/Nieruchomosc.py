class Nieruchomosc:
    def __init__(self, miasto: str, ulica: str,
                 powierzchnia: int, cena_za_m2: float):
        self._miasto = miasto
        self._ulica = ulica
        self._powierzchnia = powierzchnia
        self._cena_za_m2 = cena_za_m2

    @property
    def miasto(self) -> str:
        return self._miasto

    @property
    def ulica(self) -> str:
        return self._ulica

    @property
    def powierzchnia(self) -> int:
        return self._powierzchnia

    @property
    def cena_za_m2(self) -> float:
        return self._cena_za_m2

    def __str__(self):
        return f'Nieruchomosc polozona: ' \
               f'ul. {self._ulica} , ' \
               f'{self._miasto} ' \
               f'o {self._powierzchnia} m2 ' \
               f'cena za m2 wynosi: {self._cena_za_m2} zl. '
