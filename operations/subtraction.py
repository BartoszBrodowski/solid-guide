from operations import interface


class Subtraction(interface.Operation):
    def __init__(self, args):
        self.__args__ = args

    def calculate(self) -> int:
        # return sum(map(lambda el: int(el), self.__args__))
        return int(self.__args__[0]) - sum(map(lambda el: int(el), self.__args__[1:]))
