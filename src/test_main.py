# ----------------------------------------------
# * import block :
import unittest

from main import *

# ----------------------------------------------
# * class Test_Init : 
# ** ------------------------------------------:
class Test_Init(unittest.TestCase):
# ----------------------------------------------

# ** def test_main : 
    def test_main(self):
        with self.assertRaises(SystemExit) as cm:
            main(["main path", 
                  "--filename=Data_files/test.xlsx",
                  "--sheet_name=квартири, площі",
                  "--test"])
        self.assertEqual(cm.exception.code, 0)

# ----------------------------------------------

# ** def test_get_id : 
    def test_get_id(self):
        t = get_id("test")
        self.assertEqual(t, "test")
        t = get_id("https://youtu.be/advVd3THPAE")
        self.assertEqual(t, "advVd3THPAE")
        t = get_id("no test")
        self.assertEqual(t, "not found")


# ----------------------------------------------

# * Test runer : 
# ** ------------------------------------------:
# (compile " D:/Development/version-control/GitHub/Vadim/Tochil/main_test.py -k init")
# (compile " python -m unittest D:/Development/version-control/GitHub/Vadim/Tochil/main_test.py ")
# ** if __main__: 
if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    # runner.run(suite_Init())
    unittest.main()


# ----------------------------------------------
# * -------------------------------------------:
