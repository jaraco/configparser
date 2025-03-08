import unittest

from backports import configparser


class UnicodeBackportTestCase(unittest.TestCase):
    """Test for the backport to check if the Unicode coercion works."""

    def test_unicode_none_old_style(self):
        cp = configparser.ConfigParser(allow_no_value=True)
        cp.add_section("section")
        self.assertIsInstance(cp.sections()[0], str)
        self.assertIsInstance([sect for sect in cp][0], str)
        cp.set("section", "nothing", None)
        self.assertIsAlright(cp, None)

    def test_unicode_none_new_style(self):
        cp = configparser.ConfigParser(allow_no_value=True)
        cp["section"] = {}
        self.assertIsInstance(cp.sections()[0], str)
        self.assertIsInstance([sect for sect in cp][0], str)
        cp["section"]["nothing"] = None
        self.assertIsAlright(cp, None)

    def test_unicode_none_new_style_one_step(self):
        cp = configparser.ConfigParser(allow_no_value=True)
        cp["section"] = {'nothing': None}
        self.assertIsAlright(cp, None)

    def test_unicode_unicode_old_style(self):
        cp = configparser.ConfigParser()
        cp.add_section("section")
        self.assertIsInstance(cp.sections()[0], str)
        self.assertIsInstance([sect for sect in cp][0], str)
        cp.set("section", "nothing", "nada")
        self.assertIsAlright(cp, "nada")

    def test_unicode_unicode_new_style(self):
        cp = configparser.ConfigParser()
        cp["section"] = {}
        self.assertIsInstance(cp.sections()[0], str)
        self.assertIsInstance([sect for sect in cp][0], str)
        cp["section"]["nothing"] = "nada"
        self.assertIsAlright(cp, "nada")

    def test_unicode_unicode_new_style_one_step(self):
        cp = configparser.ConfigParser()
        cp['section'] = {'nothing': 'nada'}
        self.assertIsAlright(cp, 'nada')

    def test_unicode_extended_characters(self):
        cp = configparser.ConfigParser()
        cp.add_section('section')
        cp.add_section('łąka1')
        cp['łąka2'] = {}
        cp.set('section', 'łąka1', 'value')
        cp['section']['łąka2'] = 'value'
        self.assertEqual(set(cp['section']), {'łąka1', 'łąka2'})
        cp['new'] = {'łąka': 'value'}
        cp.set('section', 'key', 'łąka')
        cp['section']['key'] = 'łąka'
        self.assertEqual(cp['section']['key'], 'łąka')
        cp['new'] = {'key': 'łąka'}

    def assertIsAlright(self, cp, optvalue):
        self.assertIn('section', cp)
        self.assertIn('nothing', cp['section'])
        self.assertIsInstance(cp.sections()[0], str)
        self.assertIsInstance(cp.options('section')[0], str)
        self.assertEqual(cp.get('section', 'nothing'), optvalue)
        self.assertIsInstance([sect for sect in cp][0], str)
        self.assertIsInstance([opt for opt in cp['section']][0], str)
        self.assertEqual(cp['section']['nothing'], optvalue)
