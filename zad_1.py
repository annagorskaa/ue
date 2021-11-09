class Student:
    def __init__(self, name: str, marks: int) -> None:
        self._name = name
        self._marks = marks

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def marks(self) -> int:
        return self._marks

    @marks.setter
    def marks(self, value: int):
        self._marks = value

    def is_passed(self) -> bool:
        return self._marks > 50


if __name__ == '__main__':
    nn = Student('Student1', 70)
    pp = Student('Student2', 40)
    print(nn.is_passed())
    print(pp.is_passed())
