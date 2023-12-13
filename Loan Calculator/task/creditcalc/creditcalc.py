import argparse
import math

parser = argparse.ArgumentParser(description="Credit Calculator")
parser.add_argument("--type", help="Type of payment")
parser.add_argument("--payment", type=float, help="Monthly payment")
parser.add_argument("--principal", type=float, help="Credit principal")
parser.add_argument("--periods", type=int, help="Count of months")
parser.add_argument("--interest", type=float, help="Credit interest")

args = parser.parse_args()

if args.type not in ["annuity", "diff"]:
    print("Incorrect parameters")
elif args.type == "diff" and args.payment:
    print("Incorrect parameters")
elif not args.interest:
    print("Incorrect parameters")
elif args.principal is not None and args.principal < 0:
    print("Incorrect parameters")
elif args.periods is not None and args.periods < 0:
    print("Incorrect parameters")
elif args.payment is not None and args.payment < 0:
    print("Incorrect parameters")
elif args.interest is not None and args.interest < 0:
    print("Incorrect parameters")
elif args.type == "diff":
    nominal_interest = args.interest / (12 * 100)
    total = 0
    for i in range(1, args.periods + 1):
        diff_payment = math.ceil(
            args.principal / args.periods
            + nominal_interest
            * (args.principal - args.principal * (i - 1) / args.periods)
        )
        total += diff_payment
        print(f"Month {i}: paid out {diff_payment}")
    print()
    print(f"Overpayment = {total - args.principal}")
elif args.type == "annuity":
    if args.principal and args.periods:
        nominal_interest = args.interest / (12 * 100)
        annuity_payment = math.ceil(
            args.principal
            * (nominal_interest * pow(1 + nominal_interest, args.periods))
            / (pow(1 + nominal_interest, args.periods) - 1)
        )
        print(f"Your annuity payment = {annuity_payment}!")
        print(f"Overpayment = {annuity_payment * args.periods - args.principal}")
    elif args.principal and args.payment:
        nominal_interest = args.interest / (12 * 100)
        months = math.ceil(
            math.log(
                args.payment / (args.payment - nominal_interest * args.principal),
                1 + nominal_interest,
            )
        )
        years = months // 12
        months = months % 12
        if years == 0:
            print(f"You need {months} months to repay this credit!")
        elif months == 0:
            print(f"You need {years} years to repay this credit!")
        else:
            print(
                f"You need {years} years and {months} months to repay this credit!"
            )
        print(f"Overpayment = {args.payment * (years * 12 + months) - args.principal}")
    elif args.payment and args.periods:
        nominal_interest = args.interest / (12 * 100)
        credit_principal = math.floor(
            args.payment
            / (
                (nominal_interest * pow(1 + nominal_interest, args.periods))
                / (pow(1 + nominal_interest, args.periods) - 1)
            )
        )
        print(f"Your credit principal = {credit_principal}!")
        print(f"Overpayment = {args.payment * args.periods - credit_principal}")
