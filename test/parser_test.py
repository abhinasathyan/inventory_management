import unittest
from client.parser import Parser

class TestParser(unittest.TestCase):
    def test_shouldParseCommands(self):
        testObj=Parser()
        self.assertEqual( testObj.split("Brazil:100"),["Brazil","100"],msg="")
        ''' self.assertEqual(testObj.units,100,msg="")'''