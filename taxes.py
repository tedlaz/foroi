from taxes_year_selector import year_selector, Taxes


def calculate_tax(year: int, income, children=0):
    tax = year_selector.get(year, Taxes)()
    return tax.foros_eis_eea(income, children)


def ergazomenos_period_taxes(year: int, income: float, kids: int = 0, factor: int = 14) -> dict:
    tax = year_selector.get(year, Taxes)()
    return tax.foroi_period(income, kids, factor)


def mikta_apo_kathara(year: int, kathara, pefka=15, kids=0):
    tax = year_selector.get(year, Taxes)()
    return tax.mikta_apo_kathara(kathara, kids, pefka)


def mikta_apo_kathara_all(period: int, kathara, meres: int, kpk, kids: int):
    year = int(str(period)[:4])
    tax = year_selector.get(year, Taxes)()
    return tax.mikta_apo_kathara_full(period, kathara, meres, kids, kpk)


def kathara(period: int, mikta, kpk: str, kids: int):
    year = int(str(period)[:4])
    tax = year_selector.get(year, Taxes)()
    return tax.kathara_periodoy(period, mikta, kpk, kids)


if __name__ == "__main__":
    calculate_tax(2021, 14000)
