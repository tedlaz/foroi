from taxes_year_selector import year_selector, Taxes


def calculate_tax(year: int, income, children=0):
    tax = year_selector.get(year, Taxes)()
    return tax.foros_eis_eea(income, children)


if __name__ == "__main__":
    calculate_tax(2021, 14000)
