def main():
    dollars = dollars_to_float(input("How much was the meal? ").rstrip())
    percent = percent_to_float(input("What percentage would you like to tip? ").rstrip())
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    s = dollars.strip()
    d = float(s.replace("$", ""))
    return d


def percent_to_float(percent):
    p = float(percent.replace("%", "")) / 100
    return p


main()
