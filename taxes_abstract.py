import requests


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
        res["pefka"] = pefka
        res["efka"] = kratiseis_efka
        res["mikta"] = mikta_final
        return res

    def kathara_periodoy(self, period: int, mikta, kpk: str, kids: int):
        url = f"https://vwf3fo.deta.dev/kpkper?kpk={kpk}&period={period}"
        response = requests.get(url).json()
        if not response['result'][0]['kpk']:
            raise ValueError
        pefka = response['result'][0]['enos']
        pefkatotal = response['result'][0]['total']
        efka = round(mikta * pefka / 100.0, 2)
        efkatotal = round(mikta * pefkatotal / 100.0, 2)
        efkaeti = round(efkatotal-efka, 2)
        forologiteo = round(mikta - efka, 2)
        taxres = self.foroi_period(forologiteo, kids)
        return {
            'info': 'Καθαρά από μικτά περιόδου',
            'period': period,
            'mikta': round(mikta, 2),
            'kpk': kpk,
            'kids': kids,
            'efka-ergazomenoy': efka,
            'efka-ergofoti': efkaeti,
            'ekfa-total': efkatotal,
            'forologiteo': forologiteo,
            'taxdetails': taxres,
            'pliroteo': round(forologiteo - taxres['total_taxes'], 2),
            'kostos-ergodoti': round(mikta + efkaeti, 2)

        }

    def mikta_apo_kathara_full(self, period: int, kathara, meres, kids, kpk: str):
        url = f"https://vwf3fo.deta.dev/kpkper?kpk={kpk}&period={period}"
        response = requests.get(url).json()
        if not response['result'][0]['kpk']:
            raise ValueError
        pefka = response['result'][0]['enos']
        pefkatotal = response['result'][0]['total']
        txtperiod = str(period)
        month = int(txtperiod[4:])
        year = int(txtperiod[:4])
        d = round(25 / 200.0 * 1.04167, 7)
        a = round(13 / 150.0, 7)
        p = round(pefka / 100.0, 5)
        syn = 1 + d + 2 * a - p - p * d - p * a
        mikta = round((kathara / syn) / meres, 2)
        # rmikta = round(mikta * syn)
        # refka = round(mikta * p * (1 + d + a), 2)
        res = self._mikta(mikta, meres, pefka, kids)
        delta = kathara - res["clean_final"]

        i = 0
        while abs(delta) > 0.004 and i < 100:
            i += 1
            mikta += delta / meres
            mikta = round(mikta, 5)
            res = self._mikta(mikta, meres, pefka, kids)
            old_delta = delta
            delta = round(kathara - res["clean_final"], 6)
            print(mikta, delta)
            if old_delta * delta < 0:
                if delta < 0:
                    break
        # print(i)
        mikta = round(mikta, 2)
        fres = self._mikta(mikta, meres, pefka, kids)
        fres["year"] = year
        fres["month"] = month
        fres['efka_kpk'] = response['result'][0]
        return fres

    def _mikta(self, mikta, meres, pefka, kids):
        apod = round(mikta * meres, 2)
        doro = round((mikta * 25 * meres / 200.0) * 1.04167, 2)
        eadi = round(mikta * 13 * meres / 150, 2)
        adei = round(mikta * 13 * meres / 150, 2)
        tota = round(apod + doro + eadi + adei, 2)
        efka_apod = round(apod * pefka / 100.0, 2)
        efka_doro = round(doro * pefka / 100.0, 2)
        efka_eadi = round(eadi * pefka / 100.0, 2)
        efka_total = round(efka_apod + efka_doro + efka_eadi, 2)
        clean_apod = round(apod - efka_apod, 2)
        clean_doro = round(doro - efka_doro, 2)
        clean_eadi = round(eadi - efka_eadi, 2)
        clean_adei = adei
        clean_total = round(clean_apod + clean_doro +
                            clean_eadi + clean_adei, 2)
        foro_apod = self.foroi_period(clean_apod, kids)["total_taxes"]
        foro_doro = self.foroi_period(clean_doro, kids)["total_taxes"]
        foro_eadi = self.foroi_period(clean_eadi, kids, 28)["total_taxes"]
        foro_total = foro_apod + foro_doro + foro_eadi
        clean_final = round(clean_total - foro_total, 2)

        return {
            "imeromisthio": mikta,
            "meres": meres,
            "apod": apod,
            "doro": doro,
            "eadi": eadi,
            "adei": adei,
            "efka_apod": efka_apod,
            "efka_doro": efka_doro,
            "efka_eadi": efka_eadi,
            "clean_apod": clean_apod,
            "clean_doro": clean_doro,
            "clean_eadi": clean_eadi,
            "clean_adei": clean_adei,
            "foro_apod": foro_apod,
            "foro_doro": foro_doro,
            "foro_eadi": foro_eadi,
            "foro_total": foro_total,
            "dirty_total": tota,
            "efka_total": efka_total,
            "clean_total": clean_total,
            "clean_final": clean_final,
        }

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

    def foroi_period(self, apodoxes, paidia=0, barytis=14) -> dict:
        yearly = round(apodoxes * barytis, 2)
        foros_etoys = self.foros_eisodimatos(yearly, paidia)
        eea_etoys = self.foros_eea(yearly)
        tax = round(foros_etoys / barytis, 2)
        eea = round(eea_etoys / barytis, 2)
        total_taxes = round(tax + eea, 2)
        after_taxes = round(apodoxes - total_taxes, 2)
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
