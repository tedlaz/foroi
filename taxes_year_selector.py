from taxes_abstract import Taxes
from taxes_2020 import Tax2020
from taxes_2021 import Tax2021


year_selector = {
    2010: Taxes,
    2012: Taxes,
    2013: Taxes,
    2014: Taxes,
    2015: Taxes,
    2016: Taxes,
    2017: Taxes,
    2018: Taxes,
    2019: Taxes,
    2020: Tax2020,
    2021: Tax2021,
}