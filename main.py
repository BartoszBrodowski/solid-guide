import sys
import argparse
from operations import addition, subtraction


def main(args) -> int:
    """Main function..."""

    print(args)

    # instancja dodawania
    suma1 = addition.Summation(args.val)
    roznica1 = subtraction.Subtraction(args.val)
    # TODO printing out without hardcoding
    print(roznica1.calculate())

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # TODO turning on particular function on flag
    parser.add_argument("-s", "--suma", nargs="*", dest="val")
    args = parser.parse_args()
    sys.exit(main(args))
