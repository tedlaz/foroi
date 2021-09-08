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

    def mikta_apo_kathara(self, kathara, children=0, pefka=14.12):
        synt1 = 1 - pefka / 100.0
        mikto = kathara / synt1
        apot = self.foroi_period(kathara, children)
        delta = kathara - apot["after_taxes"]
        # print(pros1, delta, apot)
        i = 0
        while delta > 0 and i < 100:
            i += 1
            mikto += delta
            ap2 = self.foroi_period(mikto * synt1, children)
            delta = kathara - ap2["after_taxes"]
        mikta_final = round(mikto, 2)
        kratiseis_efka = round(mikta_final * pefka / 100.0, 2)
        forologiteo = round(mikta_final - kratiseis_efka, 2)
        res = self.foroi_period(forologiteo, children)
        res['pefka'] = pefka
        res['efka'] = kratiseis_efka
        res['mikta'] = mikta_final
        return res


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
        yearly = round(apodoxes * barytis, 2)
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
