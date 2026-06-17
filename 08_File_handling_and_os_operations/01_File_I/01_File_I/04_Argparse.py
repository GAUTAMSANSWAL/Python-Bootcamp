import argparse

parser = argparse.ArgumentParser(description="simple calculator")

parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")

parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help="Operation to perform")

args = parser.parse_args()

print(args)

if args.operation == "add":
    result = args.num1 + args.num2
elif args.operation == "sub":
    result = args.num1 - args.num2
elif args.operation == "mul":
    result = args.num1 * args.num2
elif args.operation == "div":
    if args.num2 != 0:
        result = args.num1 / args.num2
    else:
        result = "Error: Division by zero"
print(f"Result: {result}")