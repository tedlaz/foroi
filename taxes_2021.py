from taxes_abstract import Taxes
from utils import klimaka, relu


class Tax2021(Taxes):
    year = 2021

    def foros_eisodimatos(self, income, children=0):
        scale = (10000, 10000, 10000, 10000)
        syntelestes = (9, 22, 28, 36, 44)
        foros = klimaka(income, scale, syntelestes)
        paidia_meiosi_scale = {0: 777, 1: 810,
                               2: 900, 3: 1120, 4: 1340, 5: 1560}
        meiosi = paidia_meiosi_scale.get(children, paidia_meiosi_scale[5])

        if income > 12000:
            delta = income - 12000
            meiosi -= delta * 0.02
        meiosi = relu(val=meiosi)
        foros_me_meiosi = round(relu(val=foros - meiosi), 2)
        return foros_me_meiosi

    def foros_eea(self, income):
        """Για το 2021 δεν υπάρχει ΕΕΑ για τους μισθωτούς"""
        # eea_kli = (12000, 8000, 10000, 10000, 25000, 155000)
        # eea_pos = (0, 2.2, 5, 6.5, 7.5, 9, 10)
        # eea = klimaka(income, eea_kli, eea_pos)
        return 0

    def foros_enoikion(self, enoikia):
        return round(enoikia * 0.15, 2)

    def foros_tokon(self, tokoi):
        return round(tokoi * 0.15, 2)


if __name__ == "__main__":
    tax = Tax2021()
    print(tax.mikta_apo_kathara_full(202101, 249.94, 1, 0, '101'))
