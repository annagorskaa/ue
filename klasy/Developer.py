class Developer:
    def __init__(self, imie: str, nazwisko: str, wiek: int, staz: int):
        self._imie = imie
        self._nazwisko = nazwisko
        self._wiek = wiek
        self._staz = staz

    @property
    def imie(self) -> str:
        return self._imie

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @property
    def wiek(self) -> int:
        return self._wiek

    @property
    def staz(self) -> int:
        return self._staz

    def __str__(self):
        return f'Developer: {self._imie} {self._nazwisko} ' \
               f'ma {self._wiek} ' \
               f'a jego staz pracy: {self._staz} lat.'
