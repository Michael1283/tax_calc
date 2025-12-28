def calculate_income_tax():
    """
    Computes U.S. personal income tax for year 2009
    using marginal tax brackets based on filing status.
    """

    # Tax brackets: (Upper Income Limit, Tax Rate)
    single = [
        (8350, 0.10), (33950, 0.15), (82250, 0.25),
        (171550, 0.28), (372950, 0.33), (float('inf'), 0.35)
    ]

    married_joint = [
        (16700, 0.10), (67900, 0.15), (137050, 0.25),
        (208850, 0.28), (372950, 0.33), (float('inf'), 0.35)
    ]

    married_separate = [
        (8350, 0.10), (33950, 0.15), (68525, 0.25),
        (104425, 0.28), (186475, 0.33), (float('inf'), 0.35)
    ]

    head_household = [
        (11950, 0.10), (45500, 0.15), (117450, 0.25),
        (190200, 0.28), (372950, 0.33), (float('inf'), 0.35)
    ]

    tax_tables = {
        0: single,
        1: married_joint,
        2: married_separate,
        3: head_household
    }

    print("\n2009 U.S. Personal Income Tax Calculator")
    print("0 - Single")
    print("1 - Married Filing Jointly / Qualifying Widow(er)")
    print("2 - Married Filing Separately")
    print("3 - Head of Household")

    try:
        filing_type = int(input("Select filing status (0–3): "))
        if filing_type not in tax_tables:
            print("Invalid filing status selected.")
            return

        taxable_income = float(input("Enter taxable income ($): "))
        if taxable_income < 0:
            print("Income must be zero or greater.")
            return

    except ValueError:
        print("Input error: please enter numeric values only.")
        return

    # Tax computation
    total_tax = 0.0
    lower_bound = 0.0

    for upper_bound, tax_rate in tax_tables[filing_type]:
        if taxable_income > upper_bound:
            total_tax += (upper_bound - lower_bound) * tax_rate
            lower_bound = upper_bound
        else:
            total_tax += (taxable_income - lower_bound) * tax_rate
            break

    print(f"Computed Tax Payable: ${total_tax:,.2f}")


# Program entry point
calculate_income_tax()