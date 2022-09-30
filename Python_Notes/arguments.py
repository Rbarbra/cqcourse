import argparse

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument(
    "integers", metavar="N", type=int, nargs="+", help="an integer for the accumulator"
)
parser.add_argument(
    "--sum", action="store_true", help="sum the integers (default: find the max)",
)
parser.add_argument(
    "-p", "--print", action="store_true", help="print out the given integers"
)

parser.add_argument("--calc", action="store_const", const=12, default=8)

args = parser.parse_args()
if args.sum:
    print(sum(args.integers))
else:
    print(max(args.integers))
# print(args.accumulate(args.integers))
if args.print:
    print(args.integers)
print(args.calc)
