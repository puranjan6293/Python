import argparse
import sys

def calc(args):
    if args.o=="add":
        return args.x + args.y
    elif args.o=="mul":
        return args.x * args.y
    elif args.o=="sub":
        return args.x - args.y
    elif args.o=="dil":
        return args.x / args.y
    else:
        return "Something went wrong"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float,
                        default=1.0, help="Enter first number."
                                          "contact Puranjan sir ")
    parser.add_argument('--y', type=float,
                        default=2.0, help="Enter second number."
                                          "contact Puranjan sir ")
    parser.add_argument('--o', type=float,
                        default="add", help="Utility for calculating."
                                          "contact Puranjan sir ")
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
