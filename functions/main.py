import argparse
import sys
from abc import ABC, abstractmethod


class CalculatorInterface(ABC):

    @abstractmethod
    def operation(a, b):
        pass


# Bartek Brodowski
class Addition(CalculatorInterface):

    def operation(a, b):
        return a + b


def main(args):

    if args.add:
        print(Addition.operation(args.num1, args.num2))
    else:
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python")
    actionType = parser.add_mutually_exclusive_group(required=True)
    actionType.add_argument("-add", action="store_true", help="Addition")
    parser.add_argument("num1", help="First number", type=int)
    parser.add_argument("num2", help="Second number", type=int)
    args = parser.parse_args()
    main(args)
