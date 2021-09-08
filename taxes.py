from taxes_year_selector import year_selector, Taxes


def calculate_tax(year: int, income, children=0):
    tax = year_selector.get(year, Taxes)()
    return tax.foros_eis_eea(income, children)


def ergazomenos_period_taxes(year: int, income, kids=0, factor=14):
    tax = year_selector.get(year, Taxes)()
    return tax.foroi_period(income, kids, factor)


def mikta_apo_kathara(year: int, kathara, pefka=15, kids=0):
    tax = year_selector.get(year, Taxes)()
    return tax.mikta_apo_kathara(kathara, kids, pefka)


if __name__ == "__main__":
    calculate_tax(2021, 14000)
