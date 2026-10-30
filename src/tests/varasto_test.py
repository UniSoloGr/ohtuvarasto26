import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
    
    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 5)
    
    def test_str_palauttaa_oikean_merkkijonoesityksen(self):
        self.assertSequenceEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
    
    def test_negatiivisen_maaran_lisays_hylataan(self):
        init_saldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-10)
        self.assertEqual(self.varasto.saldo, init_saldo)
    
    def test_ylijaama_maara_tayttaa_varaston(self):
        max_maara = self.varasto.paljonko_mahtuu()
        self.varasto.lisaa_varastoon(max_maara + 1)
        self.assertEqual(self.varasto.saldo, self.varasto.tilavuus)
    
    def test_negatiivinen_otto_ei_muuta_saldoa(self):
        init_saldo = self.varasto.saldo
        self.varasto.ota_varastosta(-10)
        self.assertEqual(self.varasto.saldo, init_saldo)
    
    def test_ylijaama_otto_tyhjentaa_saldon(self):
        self.varasto.ota_varastosta(self.varasto.tilavuus + 1)
        self.assertEqual(self.varasto.saldo, 0)

class TestVarastoVirheellisetKonstruktoriParametrit(unittest.TestCase):
    def test_virheellinen_tilavuus_nollataan(self):
        varasto = Varasto(-10)    
        self.assertEqual(varasto.tilavuus, 0)
    
    def test_virheellinen_saldo_nollataan(self):
        varasto = Varasto(10, -10)    
        self.assertEqual(varasto.saldo, 0)
        