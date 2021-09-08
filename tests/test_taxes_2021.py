from taxes_2021 import Tax2021


def test_tax2021():
    tax = Tax2021()
    print(tax.foros_eis_eea(14000))
    print(tax.foroi_period(1000))