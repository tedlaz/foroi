from unittest import TestCase
# from decimal import Decimal
import taxes_old as tx1


class TestTaxes(TestCase):
    def test_foros_etoys(self):
        self.assertEqual(tx1.foros_etoys(2012, 110000), 36920)
        self.assertRaises(ValueError, tx1.foros_etoys, 1963, 12000)

    def test_meiosi_foroy(self):
        self.assertEqual(tx1.meiosi_foroy(2019, 200000, 0), 100)
        self.assertEqual(tx1.meiosi_foroy(2019, 1000, 5), 2100)
        self.assertEqual(tx1.meiosi_foroy(2019, 500000, 0), 0)

    def test_foros_etoys_me_ekptosi(self):
        self.assertEqual(tx1.foros_etoys_me_ekptosi(2019, 14000), 1180)

    def test_eea_etoys(self):
        self.assertEqual(tx1.eea_etoys(1985, 1000), 0)

    def test_eea_periodoy(self):
        self.assertEqual(tx1.eea_periodoy(2019, 1000, extra=100), 5.34)

    def test_foros_eea_periodoy(self):
        self.assertEqual(
            tx1.foros_eea_periodoy(2019, 1000, extra=100),
            {
                "foros": 106.29,
                "eea": 5.34,
                "forolog": 1100.00,
                "pliroteo": 988.37,
            },
        )

    def test_reverse_apodoxes(self):
        self.assertEqual(tx1.reverse_apodoxes(2019, 1250, 16, 3), 1697.99)

    def test_apodoxes(self):

        result = {
            "foros": 5.09,
            "eea": 0.0,
            "forolog": 640.0,
            "pliroteo": 634.91,
            "paidia": 0,
            "mikto": 800.00,
            "pika": "20%",
            "ika": 160.00,
            "krat": 165.09,
        }
        self.assertEqual(tx1.test_apodoxes(2019, 800.0, 20, paidia=0), result)

    def test_kostos_misthodosias(self):
        self.assertEqual(tx1.kostos_misthodosias(800, 20), 1201.8)

    def test_mikta_apo_kathara(self):
        kathara = tx1.mikta_apo_kathara(1000, 15, 0, "2019-01-01")
        self.assertEqual(kathara, 1312.16)
        kathara = tx1.mikta_apo_kathara(1000, 15, 0)
        self.assertEqual(kathara, 1292.54)

    def test_foros2020(self):
        pliroteo = tx1.foros(2021, 10159.66, 1)["pliroteo"]
        self.assertEqual(pliroteo, 10034.53)
        pliroteo = tx1.foros(2021, 13000, 3)["pliroteo"]
        self.assertEqual(pliroteo, 12518)
        pliroteo = tx1.foros(2021, 130000, 3)["pliroteo"]
        self.assertEqual(pliroteo, 71849)
        pliroteo = tx1.foros(2021, 3000, 0)["pliroteo"]
        self.assertEqual(pliroteo, 3000)
        self.assertRaises(ValueError, tx1.foros, 1980, 15000, 1)

    def test_class_foros2020(self):
        clc = tx1.Foros2020()
        self.assertEqual(clc.meiosi_foroy(15748.68), 702.03)
        self.assertEqual(clc.meiosi_foroy(14664), 723.72)
        self.assertEqual(clc.meiosi_foroy(19878.24), 619.44)
        self.assertEqual(clc.foros_enoikion(2280), 342)
        # print(clc.foros_total(19878.24, 2400, 10.62))
        res = clc.foros_total(misthoi=19878.24, enoikia=2400, tokoi=10.62)
        self.assertEqual(res['final_foros'], 2797.36)
        # print(clc.foros_total(misthoi=14000))
        print(clc.foros_misthoton_periodoy(misthos=1000))