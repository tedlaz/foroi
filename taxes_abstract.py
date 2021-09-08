class Taxes:
    year = 0

    def foros_eisodimatos(self, income, children):
        raise NotImplementedError

    def foros_eea(self, income):
        raise NotImplementedError

    def foros_enoikion(self, enoikia):
        raise NotImplementedError

    def foros_tokon(self, tokoi):
        raise NotImplementedError

    def foros_eis_eea(self, income, children=0):
        tax = self.foros_eisodimatos(income, children)
        eea = self.foros_eea(income)
        total_taxes = round(tax + eea, 2)
        after_taxes = round(income - total_taxes, 2)
        return {
            "tax_year": self.year,
            "income": income,
            "children": children,
            "tax": tax,
            "eea": eea,
            "total_taxes": total_taxes,
            "after_taxes": after_taxes,
        }

    def foroi_period(self, apodoxes, paidia=0, barytis=14):
        yearly = apodoxes * barytis
        foros_etoys = self.foros_eisodimatos(yearly, paidia)
        eea_etoys = self.foros_eea(yearly)
        tax = round(foros_etoys / barytis, 2)
        eea = round(eea_etoys / barytis, 2)
        total_taxes = round(tax + eea, 2)
        after_taxes = apodoxes - total_taxes
        return {
            "tax_year": self.year,
            "income": apodoxes,
            "children": paidia,
            "yearly_income": yearly,
            "yearly_tax": foros_etoys,
            "yearly_eea": eea_etoys,
            "tax": tax,
            "eea": eea,
            "total_taxes": total_taxes,
            "after_taxes": after_taxes,
        }
