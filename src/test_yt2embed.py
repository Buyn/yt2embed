# ----------------------------------------------
# * import block :
import unittest

from yt2embed import *

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
        # https://www.youtube.com/live/_r6YqGDSmbo?feature=share
        t = get_id("https://www.youtube.com/live/_r6YqGDSmbo?feature=share")
        self.assertEqual(t, "_r6YqGDSmbo")
        t = get_id("https://www.youtube.com/watch?v=MD3OHN3luAA&pp=ygVv0KfQtdC8INC60L7QvdGH0LDRjtGC0YHRjyDQtNC40LrRgtCw0YLRg9GA0Ysg0JjQvdGC0LXRgNCy0YzRjiDQn9Cw0LLQu9GDINCa0LDQvdGL0LPQuNC90YMg0LrQsNC90LDQuyBwcm9zbGVkdWV0")
        self.assertEqual(t, "MD3OHN3luAA")
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
