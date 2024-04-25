import csv
import unittest
from specaillecture.CSVPrinter import CSVPrinter
import os.path

class TestCSVPrinter(unittest.TestCase):

    def test_read(self):

        try:
            printer = CSVPrinter("sample.csv")
            l = printer.read()
        except :
            print("-1")
        file_path = os.path.join(os.path.dirname(__file__), "sample.csv")
        printer = CSVPrinter(file_path)
        l = printer.read()
        
        line = len (l)
        row = len(l[0])

        self.assertEqual(2,row)
        self.assertEqual(2,line)
        self.assertEqual(2, len(l))  # add assertion here


if __name__ == '__main__':
    unittest.main()

