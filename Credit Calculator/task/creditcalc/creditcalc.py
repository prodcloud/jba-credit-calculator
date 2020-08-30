import sys  # first, we import the module
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str,
                    help="Payment type: annuity or diff (differentiated)")
parser.add_argument("--payment", type=int,
                    help="Monthly payment")
parser.add_argument("--principal", type=int,
                    help="Loan principal amount")
parser.add_argument("--periods", type=int,
                    help="Loan payment periods")
parser.add_argument("--interest", type=float,
                    help="Loan interest rate")

args = parser.parse_args()

if not args.type:

    print("Incorrect parameters")
    sys.exit(1)

elif args.type == "diff":

    if args.payment:
        print("Incorrect parameters")
        sys.exit(1)

    credit_principal = args.principal
    current_month = int(1)
    interest = args.interest
    period = args.periods
    payment_total = 0

    if credit_principal < 0 or interest < 0 or period < 0:
        print("Incorrect parameters")
        sys.exit(1)

    while current_month <= period:
        i = interest / (12 * 100)
        monthly_payment = math.ceil((credit_principal / period) +
                                    (i * (credit_principal - ((credit_principal * (current_month - 1)) / period))))
        print(f"Month {current_month}: payment is {monthly_payment}")
        current_month += 1
        payment_total += monthly_payment

    overpayment = payment_total - credit_principal
    print(f"\nOverpayment: {overpayment}")

elif args.type == "annuity":

    if len(sys.argv) < 5 or not args.interest:
        print("Incorrect parameters")
        sys.exit(1)

    if not args.payment:

        credit_principal = args.principal
        interest = args.interest
        period = args.periods

        if credit_principal < 0 or interest < 0 or period < 0:
            print("Incorrect parameters")
            sys.exit(1)

        i = interest / (12 * 100)
        payment = math.ceil(credit_principal * ((i * (1 + i) ** period) / ((1 + i) ** period - 1)))

        print(f"Your annuity payment = {payment}!")
        overpayment = math.ceil(payment * period - credit_principal)
        print(f"Overpayment: {overpayment}")

    elif not args.periods:

        credit_principal = args.principal
        interest = args.interest
        payment = args.payment

        if credit_principal < 0 or interest < 0 or payment < 0:
            print("Incorrect parameters")
            sys.exit(1)

        i = interest / (12 * 100)

        period = math.ceil(math.log(payment / (payment - i * credit_principal), 1 + i))

        years = math.floor(period / 12)
        remaining_months = int(period % 12)

        if remaining_months == 0:
            print("It will take {0} years to repay this credit!".format(years))
        elif years <= 0:
            print("It will take {0} months to repay this credit!".format(remaining_months))
        else:
            print("It will take {0} years and {1} months to repay this credit!".format(years, remaining_months))

        overpayment = payment * period - credit_principal
        print(f"Overpayment = {overpayment}")

    else:
        payment = args.payment
        interest = args.interest
        period = args.periods

        if payment < 0 or interest < 0 or period < 0:
            print("Incorrect parameters")
            sys.exit(1)

        i = interest / (12 * 100)
        credit_principal = math.floor(payment / ((i * (1 + i) ** period) / ((1 + i) ** period - 1)))

        print(f"Your credit principal = {credit_principal}!")
        overpayment = math.ceil(payment * period - credit_principal)
        print(f"Overpayment: {overpayment}")
else:
    print("Incorrect parameters")
    sys.exit(1)
