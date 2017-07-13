import unittest
from online_store.store import OnlineStore

class TestStore(unittest.TestCase):
    def test_calculateSP(self):
        test_obj=OnlineStore()
        self.assertFalse(test_obj.CalculateSP(100,100,0),msg="units cannot be zero")
        self.assertEqual(test_obj.CalculateSP(100,100,100),10000,msg="")

